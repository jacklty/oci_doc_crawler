import urllib.robotparser
rp = urllib.robotparser.RobotFileParser()
rp.set_url("https://docs.oracle.com/robots.txt")
rp.read()
rp.can_fetch("*", "https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengoverview.htm")