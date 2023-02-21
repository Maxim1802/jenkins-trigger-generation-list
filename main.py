import os
#import re

from github_action_utils import set_output
from github_action_utils import save_state

def main():

  ns = os.environ["INPUT_NAMESPACE"]
  #stage = os.environ["INPUT_STAGE"]
  jobs_path_string = os.environ["INPUT_JOBS_PATH_STRING"]

  jobs_list = []
  jobs_string = ""

  #print(re.sub("[a-z]*@", "abc@", jobs_string))
  #print(re.sub("^\[|]$", "", jobs_string))

  for i in jobs_path_string.split(" "):
    jobs_list.append('%s-%s-%s' % (ns,i.split("/")[1],(i.split("/")[-1]).replace(".yaml","")))

  jobs_string = ','.join(jobs_list) 

  print(jobs_string)

  set_output("jobs_string", jobs_string)
  save_state("jobs_string", jobs_string)

if __name__ == "__main__":
  main()