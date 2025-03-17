Updated 2023-09-26
# Managing Path Route Sets
On Compute Cloud@Customer, you can apply a set of _path routes_ to an LBaaS resource. 
A path route is a string that the load balancer matches against an incoming URI to determine the appropriate destination backend set. Some applications have multiple endpoints or content types, each distinguished by a unique URI path. For example, `/admin/`, `/data/`, `/video/`, or `/cgi/`. 
The idea behind path route sets is to conserve resources. With path route sets, you can use the path route rules to route traffic to the correct backend set without using multiple listeners or load balancers.
Path route rules apply _only_ to HTTP and HTTPS requests and have no effect on TCP requests.
A _path route set_ includes all path route rules that define the data routing for a particular listener.
**Note** Path route sets have several restrictions: 
  * You can't use asterisks in path route strings.
  * You can't use regular expressions.
  * Path route string matching is case-insensitive (that is, "data" or "DATA" is a match).
  * You can specify up to 20 path route rules for each path route set.
  * You can have one path route set for each listener. The maximum number of listeners limits the number of path route sets you can specify for a load balancer.
  * Browsers often add an ending slash to the path in a request. If you specify a path such as `/admin`, you might want to configure the path both with and without the trailing slash. For example,`/admin` and `/admin/`.


Generally, a path route rule consists of a path route string and a pattern match type. The string is some element of the URI path, for example, `/video/`, or `/cgi/`. The pattern match can be: 
  * EXACT_MATCH: The path string must match the incoming URI path exactly. 
  * FORCE_LONGEST_PREFIX_MATCH: The path string must match longest ("best") match of the _beginning_ portion of the incoming URI path.
  * PREFIX_MATCH: The path string must match the beginning portion of the incoming URI path.
  * SUFFIX_MATCH: The path string must match the ending portion of the incoming URI path.


Was this article helpful?
YesNo

