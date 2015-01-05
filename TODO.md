
 * process_name handling in register process:
   * ```for x in [x for x in os.listdir("/proc") if re.match(r"^\d+$", x)]```
   * get the contents of "/proc/%s/cmdline" % (x,)
   * match name against it
   * save x into a list and record the pids found for callbacks with action
   * save process_name for matching on each exec event