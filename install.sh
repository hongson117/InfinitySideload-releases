#!/bin/sh
# Cài đặt ∞Sideload trực tiếp trên iPhone/iPad (iOS 27+) không cần máy tính qua Open Minis.
#
# Cách chạy trong Terminal của Open Minis (1.16+) với LocalDevVPN:
#   wget -qO- https://raw.githubusercontent.com/hongson117/InfinitySideload-releases/main/install.sh | sh
#
# Dự phòng qua CDN jsDelivr (nếu mạng chặn raw.githubusercontent.com):
#   wget -qO- https://fastly.jsdelivr.net/gh/hongson117/InfinitySideload-releases@main/install.sh | sh
set -eu

REPO="hongson117/InfinitySideload-releases"
TAG="v0.1.0-b1077"
SHA256="5405e388ee45612a9d0f94665ad1d0f3237d1ac73ba375fc99c8cf69e9372efc"
SIZE=10175504
UNSET_MARKER="UNSET_""SHA256"

SOURCES="https://github.com/$REPO/releases/download/$TAG/isl-boot-aarch64
https://github.com/$REPO/releases/latest/download/isl-boot-aarch64"
SOURCES="${ISL_BOOT_SOURCES:-$SOURCES}"

DIR="$HOME/.isl-boot/bin"
BIN="$DIR/isl-boot"

say_ok()   { printf '  \033[1;32m✓\033[0m %s\n' "$1"; }
say_warn() { printf '  \033[1;33m▲\033[0m %s\n' "$1"; }
say_fail() { printf '  \033[1;31m✗\033[0m %s\n' "$1" >&2; exit 1; }

case "$(uname -m)" in
  aarch64 | arm64) ;;
  *) say_fail "isl-boot chỉ chạy trong Open Minis trên iPhone/iPad (aarch64); thiết bị hiện tại là $(uname -m)." ;;
esac

fetch_file() {
  if command -v curl >/dev/null 2>&1; then
    curl -fsSL --connect-timeout 20 -y 30 -Y 1 "$1" -o "$2"
  else
    wget -q -T 30 -O "$2" "$1"
  fi
}

sha_of() {
  sha256sum "$1" | cut -d ' ' -f 1
}

verify_or_accept() {
  actual="$(sha_of "$1")"
  if [ -z "$SHA256" ] || [ "$SHA256" = "$UNSET_MARKER" ]; then
    [ -s "$1" ] && return 0
    return 1
  fi
  [ "$actual" = "$SHA256" ]
}

mkdir -p "$DIR"

if [ -f "$BIN" ] && [ -n "$SHA256" ] && [ "$SHA256" != "$UNSET_MARKER" ] && [ "$(sha_of "$BIN")" = "$SHA256" ]; then
  say_ok "isl-boot đã ở phiên bản mới nhất ($TAG)"
else
  got=""
  for url in $SOURCES; do
    rm -f "$BIN.part"
    printf '  \033[36m⋯\033[0m Đang tải bộ cài mồi ∞Sideload (%s)…\n' "$TAG"
    if fetch_file "$url" "$BIN.part" && verify_or_accept "$BIN.part"; then
      got="$url"
      break
    fi
    say_warn "Không tải hoặc xác thực được từ nguồn đầu, đang thử nguồn tiếp theo…"
    rm -f "$BIN.part"
  done
  if [ -z "$got" ]; then
    rm -f "$BIN.part"
    say_fail "Không tải được isl-boot hoặc mã SHA-256 không khớp. Hãy kiểm tra kết nối mạng (tạm tắt LocalDevVPN nếu đang mất mạng rồi chạy lại)."
  fi
  chmod 755 "$BIN.part"
  mv "$BIN.part" "$BIN"
  say_ok "Đã tải và xác thực SHA-256 thành công cho isl-boot"
fi

ln -sf "$BIN" /usr/local/bin/isl-boot 2>/dev/null || true

if [ -t 0 ]; then
  exec "$BIN" "$@"
elif [ -r /dev/tty ] && (: < /dev/tty) 2>/dev/null; then
  exec "$BIN" "$@" < /dev/tty
else
  exec "$BIN" "$@"
fi
