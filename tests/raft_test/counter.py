import sys
import time

sys.path.append("../../")

from todo_grud.cache.raft_protocol.sync_client_cache import SyncClientIDCache

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: %s self_port partner1_port partner2_port ...' % sys.argv[0])
        sys.exit(-1)

    port = int(sys.argv[1])
    partners = [f'localhost:{p}' for p in sys.argv[2:]]
    o = SyncClientIDCache(f'localhost:{port}', partners)
    old_value = None
    key = 'counter'
    while True:

        time.sleep(0.5)

        value = o.get(key)
        if value != old_value and value is not None:
            old_value = value
            print(f"old value {old_value}")

        if old_value is not None and old_value >= 50:
            print("Pass in test!")
            break

        if port == 3000 and o.get_leader():
            if o.get(key) is None:
                o.add(key, 10)
            else:
                o.remove(key)
                o.add(key, old_value + 10)
