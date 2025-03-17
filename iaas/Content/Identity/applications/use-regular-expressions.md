Updated 2023-04-14
# Using Regular Expressions
Use regular expressions (regex) to define a URL pattern which represents more than one URL of your enterprise application and for which you can apply the same authentication policy and the same authorization policy.
Create a list of all URLs for your application, and then to define URL patterns that map similar URLs, in which you want to define common authentication and authorization policies.
The authorization engine of App Gateway supports all tokens available to create regular expressions, such as Character Classes, Anchors, Escaped Characters, Group & References, Lookaround, Quantifiers & Alternation, and Substitution.
The following is a list of common operators supported by App Gateway's authorization engine:
Common Regex Operators Supported by App Gateway Authorization Engine Operator | Description | Example  
---|---|---  
**Match-any-character Operator (`.`)** | The period character represents this operator. | `a.b` matches any three-character string beginning with `a` and ending with `b`  
**Match-zero-or-more Operator (`*`)** | This operator repeats the smallest possible preceding regular expression as many times as necessary (including zero) to match the pattern | `a*` matches any string made up of zero or more `a`'s. In another example, `fo*` has a repeating `o`, not a repeating `fo`. Hence, `fo*` matches `f`, `fo`, `foo`, and so on.  
**Match-one-or-more Operator (`+`)** | This operator is similar to the match-zero-or-more operator except that it repeats the preceding regular expression at least once. | `ca+r` matches `car` and `caaaar`, but not `cr`  
**Match-zero-or-one Operator (`?`)** | This operator is similar to the match-zero-or-more operator except that it repeats the preceding regular expression once or not at all. | `ca?r` matches both `car` and `cr`, but nothing else.  
**Negate (`^`)** | Negate an expression. | `^a` matches any character except `a`  
****Grouping Operators (`(...)`) **** | Regex treats expressions inside the parenthesis just as mathematics and programming languages treat a parenthesized expression as a unit. The expressions are processed before the expression outside the parenthesis. | `f(a|b)a` matches `faa` and `fba`, which means the operation `a|b` is processed before the rest.  
**Alternation Operator (`|`)** | Alternatives match one of a choice of regular expressions: if you put one or more characters representing the alternation operator between any two regular expressions `a` and `b`, the result matches the union of the strings that `a` and `b` match. |  `foo|bar|quux` would match any of `foo`, `bar` or `quux` As another example, `(` and `)` are the open and close-group operators, then `fo(o|b)ar` would match either `fooar` or `fobar`. On the other hand, `foo|bar` would match `foo` or `bar`  
**List Operators (`[ ... ]` and `[^ ... ]`) ** |  A matching list matches a single character represented by one of the list items. An item is a character, a character class expression, or a range expression. Non matching lists are similar to matching lists except that they match a single character not represented by one of the list items. |  `[ab]` matches either `a` or `b`. `[ad]*` matches the empty string and any string composed of just `a`'s and `d`'s in any order. As a non matching example, `[^ab]` matches any character except `a` or `b`  
**Range Operator (`-`) ** | Represents those characters that fall between two elements in the current collating sequence. | `[a-f]` represents all the characters from `a` through `f` inclusively.  
**Digit (`\d`)** | Matches any digit character (0-9). | Same as `[0-9]`  
**Not Digit (`\D`)** | Matches any character that is not a digit character (0-9). | Same as `[^0-9]`  
**Escape (`\`)** | Makes the next character in the expression means the character itself but not an operator. | `\.` means period, not the Match-any-character operator.  
## Use of Regular Expression 🔗 
For example, if you want to allow only authenticated users access for any page of the application that starts with `my` and are under the path `/mybank`, then you can use the regular expression `/mybank/my.*`
The dot (.) and the star (*) together represents any sequence of zero or more consecutive characters after the prefix `my`.
In this example, the URLs `/mybank/myCredits` and `/mybank/myDebits` match the `/mybank/my.*` pattern, but `/mybank/about` doesn't.
Was this article helpful?
YesNo

