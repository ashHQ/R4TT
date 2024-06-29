# R4TT

R4TT is a fast flexible and python based crawler



## Usage
```bash
                      .
 j.                  ,W
 EW,                i## GEEEEEEEL GEEEEEEEL
 E##j              f### ,;;L#K;;. ,;;L#K;;.
 E###D.           G####    t#E       t#E
 E#jG#W;        .K#Ki##    t#E       t#E
 E#t t##f      ,W#D.,##    t#E       t#E
 E#t  :K#E:   i##E,,i##,   t#E       t#E
 E#KDDDD###i ;DDDDDDE##DGi t#E       t#E
 E#f,t#Wi,,,        ,##    t#E       t#E
 E#t  ;#W:          ,##    t#E       t#E
 DWi   ,KK:         .E#     fE        fE
                      t      :         :    V.01


usage: r4tt.py [-h] [-u root] [-c cook] [-r regex] [-e {csv,json}] [-o output] [-l level] [-t threads] [-d delay] [-v] [-s seeds [seeds ...]] [--stdout std] [--user-agent user_agent]
               [--exclude exclude] [--timeout timeout] [-p proxies] [--clone] [--headers] [--dns] [--keys] [--update] [--only-urls] [--wayback]

options:
  -h, --help            show this help message and exit
  -u root, --url root   root url
  -c cook, --cookie cook
                        cookie
  -r regex, --regex regex
                        regex pattern
  -e {csv,json}, --export {csv,json}
                        export format
  -o output, --output output
                        output directory
  -l level, --level level
                        levels to crawl
  -t threads, --threads threads
                        number of threads
  -d delay, --delay delay
                        delay between requests
  -v, --verbose         verbose output
  -s seeds [seeds ...], --seeds seeds [seeds ...]
                        additional seed urls
  --stdout std          send variables to stdout
  --user-agent user_agent
                        custom user agent(s)
  --exclude exclude     exclude urls matching this regex
  --timeout timeout     http request timeout
  -p proxies, --proxy proxies
                        proxy server ip:port or domain:port
  --clone               clone the website locally
  --headers             add headers
  --dns                 enumerate subdomains and dns data
  --keys                find secret keys
  --update              update photon
  --only-urls           only extract urls
  --wayback             fetch urls from archive.org as seeds

```
## License

[MIT](https://choosealicense.com/licenses/mit/)
