# Volatile Memory (Virtual Memory?)

1. When given a suspended VM, there often will be a .vmem file; copy it out!

2. Use the free tool volatility to conduct analysis.
  * <pre>volatility -f FILE imageinfo</pre>
    * Get a summary of the image (OS running, etc)
  * <pre>volatility -f FILE pslist</pre>
    * Get a list of running processes; doesn't show some.
  * <pre>volatility -f FILE psscan</pre>
    * Get more running processes; more thorough
  * <pre>volatility -f FILE consoles</pre>
    * Get the data running in and command prompts
  * <pre>volatility -f FILE connections</pre>
    * 
  * <pre>volatility -f FILE connscan</pre>
