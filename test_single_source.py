'''
Script để test từng nguồn proxy bị comment một cách riêng lẻ.
Chạy: python test_single_source.py
'''
import sys
import traceback

# Danh sách các nguồn bị comment cần test
COMMENTED_SOURCES = [
    'spysone',
    'jiliuip',
    'iplocate',
    'proxifly',
    'proxyhub',
    'proxylist',
    'thespeedx',
    'tomcat1235',
    'freeproxydb',
]

def test_source(source_name):
    """Test một nguồn proxy cụ thể"""
    print(f"\n{'='*60}")
    print(f"Testing: {source_name}")
    print('='*60)

    try:
        # Dynamic import
        module = __import__(f'freeproxy.modules.proxies.{source_name}', fromlist=[''])

        # Tìm class ProxiedSession trong module
        class_name = None
        for name in dir(module):
            if 'ProxiedSession' in name and name != 'BaseProxiedSession':
                class_name = name
                break

        if not class_name:
            print(f"  ❌ Không tìm thấy class ProxiedSession trong module {source_name}")
            return False

        print(f"  📦 Found class: {class_name}")

        # Khởi tạo session
        session_class = getattr(module, class_name)
        session = session_class()

        print(f"  🌐 Homepage: {session.homepage}")
        print(f"  🔄 Đang lấy proxies...")

        # Gọi refreshproxies để lấy danh sách proxy
        session.refreshproxies()
        proxies = session.candidate_proxies

        # Hiển thị tối đa 5 proxy
        max_show = min(5, len(proxies))
        for i in range(max_show):
            proxy = proxies[i]
            print(f"    → Proxy {i+1}: {proxy.ip}:{proxy.port} ({proxy.protocol})")

        if proxies:
            print(f"  ✅ SUCCESS! Lấy được {len(proxies)} proxies")
            return True
        else:
            print(f"  ⚠️ Không lấy được proxy nào")
            return False

    except ImportError as e:
        print(f"  ❌ Import Error: {e}")
        return False
    except Exception as e:
        print(f"  ❌ Error: {e}")
        traceback.print_exc()
        return False


def main():
    print("="*60)
    print("TEST CÁC NGUỒN PROXY BỊ COMMENT")
    print("="*60)

    # Nếu có argument, chỉ test nguồn đó
    if len(sys.argv) > 1:
        source = sys.argv[1]
        if source in COMMENTED_SOURCES:
            test_source(source)
        else:
            print(f"Nguồn '{source}' không nằm trong danh sách.")
            print(f"Các nguồn có thể test: {', '.join(COMMENTED_SOURCES)}")
        return

    # Test tất cả các nguồn
    results = {}
    for source in COMMENTED_SOURCES:
        results[source] = test_source(source)

    # Tổng kết
    print("\n" + "="*60)
    print("TỔNG KẾT")
    print("="*60)

    working = [s for s, ok in results.items() if ok]
    not_working = [s for s, ok in results.items() if not ok]

    print(f"\n✅ Hoạt động ({len(working)}):")
    for s in working:
        print(f"   - {s}")

    print(f"\n❌ Không hoạt động ({len(not_working)}):")
    for s in not_working:
        print(f"   - {s}")

    print("\n" + "="*60)
    print("Để uncomment các nguồn hoạt động, chỉnh sửa file:")
    print("freeproxy/modules/proxies/__init__.py")
    print("="*60)


if __name__ == '__main__':
    main()
