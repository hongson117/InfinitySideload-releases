"""Publish audited unsigned Sideload + SideloadRunner1 + SideloadRunner2 code; never accepts user signing data."""
import base64, hashlib, json, os, pathlib, subprocess, sys, urllib.request, zipfile, plistlib

repo = os.environ["GITHUB_REPOSITORY"]
assert repo in ("hongson117/InfinitySideload-releases", "hongson117/iSideload-releases")
root = pathlib.Path(sys.argv[1])
ipa = root / "Sideload.ipa"
r1_ipa = root / "SideloadRunner1.ipa"
r2_ipa = root / "SideloadRunner2.ipa"


def command(*args):
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stderr)
    return result.stdout.strip()


meta = json.loads((root / "BUILD-SOURCE.json").read_text())
audit = json.loads((root / "recipient-audit.json").read_text())
assert audit["passed"] and not audit["failures"]
r1_audit = json.loads((root / "runner1-audit.json").read_text())
assert r1_audit["passed"] and not r1_audit["failures"]
r2_audit = json.loads((root / "runner2-audit.json").read_text())
assert r2_audit["passed"] and not r2_audit["failures"]

sha = hashlib.sha256(ipa.read_bytes()).hexdigest()
r1_sha = hashlib.sha256(r1_ipa.read_bytes()).hexdigest()
r2_sha = hashlib.sha256(r2_ipa.read_bytes()).hexdigest()
sums = (root / "SHA256SUMS.txt").read_text()
assert sha in sums and r1_sha in sums and r2_sha in sums

with zipfile.ZipFile(ipa) as z:
    info = plistlib.loads(z.read(next(n for n in z.namelist() if n.count("/") == 2 and n.endswith(".app/Info.plist"))))
assert info["CFBundleIdentifier"] == "com.hongson117.sicontainer"
assert info["CFBundleShortVersionString"] == meta["version"] and str(info["CFBundleVersion"]) == meta["build"]
assert info["ISLGitSHA"] == meta["source_commit"][:7]

with zipfile.ZipFile(r1_ipa) as z:
    r1_info = plistlib.loads(z.read(next(n for n in z.namelist() if n.count("/") == 2 and n.endswith(".app/Info.plist"))))
assert r1_info["CFBundleIdentifier"] == "com.hongson117.sicontainer.runner1"
assert r1_info["CFBundleShortVersionString"] == meta["version"] and str(r1_info["CFBundleVersion"]) == meta["build"]
assert r1_info["ISLGitSHA"] == meta["source_commit"][:7]

with zipfile.ZipFile(r2_ipa) as z:
    r2_info = plistlib.loads(z.read(next(n for n in z.namelist() if n.count("/") == 2 and n.endswith(".app/Info.plist"))))
assert r2_info["CFBundleIdentifier"] == "com.hongson117.sicontainer.runner2"
assert r2_info["CFBundleShortVersionString"] == meta["version"] and str(r2_info["CFBundleVersion"]) == meta["build"]
assert r2_info["ISLGitSHA"] == meta["source_commit"][:7]

tag = f"v{meta['version']}-b{meta['build']}"
notes = root / "release-notes.md"
notes.write_text(
    f"""∞Sideload {meta['version']} · Build {meta['build']} (Adaptive 2–3 Containers Zero-Config · VI/EN)

- Hỗ trợ đầy đủ song ngữ Tiếng Việt & Tiếng Anh (VI/EN) cho cả ứng dụng, Widget và bộ cài USB Windows/macOS.
- Bật mục "Cài cho iPhone khác" (Install on Another iPhone) trực tiếp trong tab Cài đặt và mục Thiết bị & Ghép đôi.
- Kiến trúc tự động thích ứng 2–3 Container (`∞Sideload` Chính + `∞Sideload 1` + `∞Sideload 2`) hoàn toàn tự động (Zero-Config).
- Tự động nhận diện và bảo vệ ứng dụng phát nhạc/âm thanh nền + Ghim giữ phát nền thủ công (Pin).

IPA chưa ký (`Sideload.ipa` đã kèm sẵn `SideloadRunner1.ipa` và `SideloadRunner2.ipa` bên trong để tự động cài đặt).
""",
    encoding="utf-8",
)
assets = [
    ipa,
    r1_ipa,
    r2_ipa,
    root / "SHA256SUMS.txt",
    root / "ThirdPartyNotices.txt",
    root / "BUILD-SOURCE.json",
    root / "recipient-audit.json",
    root / "runner1-audit.json",
    root / "runner2-audit.json",
]
for extra_zip in ("isl-windows.zip", "isl-macos-universal.zip"):
    extra_path = pathlib.Path(extra_zip)
    if extra_path.exists():
        assets.append(extra_path)
exists = subprocess.run(["gh", "release", "view", tag, "--repo", repo], capture_output=True).returncode == 0
if not exists:
    command(
        "gh",
        "release",
        "create",
        tag,
        *map(str, assets),
        "--repo",
        repo,
        "--latest",
        "--title",
        f"∞Sideload {meta['version']} · Build {meta['build']}",
        "--notes-file",
        str(notes),
    )
url = f"https://github.com/{repo}/releases/download/{tag}/Sideload.ipa"
r1_url = f"https://github.com/{repo}/releases/download/{tag}/SideloadRunner1.ipa"
r2_url = f"https://github.com/{repo}/releases/download/{tag}/SideloadRunner2.ipa"
with urllib.request.urlopen(url, timeout=120) as response:
    assert hashlib.file_digest(response, "sha256").hexdigest() == sha
with urllib.request.urlopen(r1_url, timeout=120) as response:
    assert hashlib.file_digest(response, "sha256").hexdigest() == r1_sha
with urllib.request.urlopen(r2_url, timeout=120) as response:
    assert hashlib.file_digest(response, "sha256").hexdigest() == r2_sha


def order(entry):
    return tuple(int(n) for n in entry["version"].split(".")) + (int(entry["build"]),)


for attempt in range(3):
    current = json.loads(command("gh", "api", f"repos/{repo}/contents/app-updates.json"))
    manifest = json.loads(base64.b64decode(current["content"]))
    entry = {"version": meta["version"], "build": meta["build"], "url": url, "sha256": sha, "bytes": ipa.stat().st_size}
    old = manifest["apps"].get("sicontainer")
    if old and order(old) > order(entry):
        break
    if old == entry:
        break
    manifest["apps"]["sicontainer"] = entry
    content = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode()
    request = root / "feed-request.json"
    request.write_text(
        json.dumps(
            {
                "message": f"Publish ∞Sideload {meta['version']} build {meta['build']} update",
                "sha": current["sha"],
                "content": base64.b64encode(content).decode(),
            }
        )
    )
    result = subprocess.run(
        ["gh", "api", "--method", "PUT", f"repos/{repo}/contents/app-updates.json", "--input", str(request)],
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        break
else:
    raise RuntimeError("Release uploaded but update feed requires retry")

print(json.dumps({"published": True, "ipa": url, "sha256": sha, "runner1_ipa": r1_url, "runner1_sha256": r1_sha, "runner2_ipa": r2_url, "runner2_sha256": r2_sha}))
