# Website Forensics

1. Fuzz around. Don't jump to the source immediately; you WILL miss something.

2. Reverse DNS and Subdomain Finder
  * [https://pentest-tools.com/information-gathering/find-subdomains-of-domain](https://pentest-tools.com/information-gathering/find-subdomains-of-domain)

3. View the source code. Look for anything interesting.
  * Comments?
  * Source Files, such as JS scripts, CSS includes?
  * 

4. <b>nmap</b> scan of the website.
  * Directories of interest
    1. /.git/
  * URLs of interest
    1. .htaccess
    2. robots.txt
    3. 
  * Can you enumerate through the directories?
  * <pre>nmap --script http-enum --script-args http-enum.displayall IP</pre>
  * Port Scan, just in case.
    * <pre>nmap -Pn IP</pre> (Check to see if this is right command!)
    * <pre>sudo nmap -sS IP</pre>

5. Take a look at the cookies.
  * EditThisCookie

6. Maybe you should access the website through another method, such as POST or HEAD.
  * Use Postman with Chrome Interceptor for this.

7. DNS Lookup
  * Don't have a good tool for this one; search the internet for it.
  * [https://www.ultratools.com/tools/dnsLookup](https://www.ultratools.com/tools/dnsLookup)
