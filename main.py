import os

def main():
  jobs_json = os.environ["INPUT_JOBS_JSON"]
  print(jobs_json)

  print(f"::set-output name=build_url::{build_url}")
  print(f"::notice title=build_url::{build_url}")

if __name__ == "__main__":
  main()