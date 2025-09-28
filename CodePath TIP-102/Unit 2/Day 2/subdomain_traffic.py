'''
Problem 4: Gallery Subdomain Traffic
Your gallery has been trying to increase it's online presence by hosting several virtual galleries. 
Each virtual gallery's web traffic is tracked through domain names, where each domain may have subdomains.

A domain like "modern.artmuseum.com" consists of various subdomains. At the top level, we have "com", at the next level, 
we have "artmuseum.com", and at the lowest level, "modern.artmuseum.com". When visitors access a domain like "modern.artmuseum.com", 
they also implicitly visit the parent domains "artmuseum.com" and "com".

A count-paired domain is represented as "rep d1.d2.d3" where rep is the number of visits to the domain and d1.d2.d3 is the domain itself.

For example, "9001 modern.artmuseum.com" indicates that "modern.artmuseum.com" was visited 9001 times.
Given an array of count-paired domains cpdomains, return an array of the count-paired domains of each subdomain. 
The order of the output does not matter.

def subdomain_visits(cpdomains):
    pass
    
Example Usage:
cpdomains1 = ["9001 modern.artmuseum.com"]
cpdomains2 = ["900 abstract.gallery.com", "50 impressionism.com", 
              "1 contemporary.gallery.com", "5 medieval.org"]

print(subdomain_visits(cpdomains1))
print(subdomain_visits(cpdomains2))

Example Output:
["9001 artmuseum.com", "9001 modern.artmuseum.com", "9001 com"]

["901 gallery.com", "50 impressionism.com", "900 abstract.gallery.com", "5 medieval.org", "5 org",
"1 contemporary.gallery.com", "951 com"]
'''

def subdomain_visits(cpdomains):
    if not cpdomains:
        return []
    
    # Dictionary to hold the count of visits for each subdomain.
    visit_counts = {}
    for cpdomain in cpdomains:
        count, domain = cpdomain.split()
        count = int(count)
        subdomains = domain.split('.')

        # Generate all possible subdomains and update their visit counts.
        for i in range(len(subdomains)):
            subdomain = '.'.join(subdomains[i:])
            visit_counts[subdomain] = visit_counts.get(subdomain, 0) + count

    # Prepare the result in the required format.
    result = [f"{count} {domain}" for domain, count in visit_counts.items()]
    return result

cpdomains1 = ["9001 modern.artmuseum.com"]
cpdomains2 = ["900 abstract.gallery.com", "50 impressionism.com", 
              "1 contemporary.gallery.com", "5 medieval.org"]

print(subdomain_visits(cpdomains1))
print(subdomain_visits(cpdomains2))