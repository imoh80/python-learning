global_sales = 0


def make_drink():
    """Demonstrate local and global variable lifetime."""
    local_count = 0
    global global_sales

    local_count += 1
    global_sales += 1

    print(f"Local: {local_count}, Global: {global_sales}")


make_drink()
make_drink()