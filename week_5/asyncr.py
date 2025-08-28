import asyncio
import time


async def download_file(file_name, seconds):
    """Simulate downloading a file and report its elapsed time."""
    print(f"Downloading {file_name}...")
    start = time.perf_counter()
    await asyncio.sleep(seconds)  # non-blocking delay
    elapsed = time.perf_counter() - start
    print(f"Finished {file_name} (took {elapsed:.2f}s)")


async def main():
    total_start = time.perf_counter()
    tasks = [
        download_file("file1.txt", 3),
        download_file("file2.txt", 2),
        download_file("file3.txt", 1),
    ]
    await asyncio.gather(*tasks)
    total_elapsed = time.perf_counter() - total_start
    print(f"All downloads finished in {total_elapsed:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())
