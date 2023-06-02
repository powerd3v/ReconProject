# pip install dnspython
import dns.resolver

# Create a class to represent a DNS resolver
class DNSResolver:
    # The get_dns method performs a DNS query to get the list of name servers for the domain
    def get_dns(self, domain):
        # Perform a DNS query to get the list of name servers for the domain
        ns = dns.resolver.query(domain, 'NS')
    
        # Iterate over the name servers and perform a DNS lookup for each of them
        results = []
        for server in ns:
            server = str(server)
            subdomain = "api"
    
            # Try to perform a DNS lookup for the subdomain
            try:
                answers = dns.resolver.query(subdomain + "." + domain, "A")
    
                # Iterate over the IP addresses returned by the DNS lookup and add them to the results list
                for ip in answers:
                    txt = subdomain + "." + domain + " - " + str(ip)
                    print(txt)
                    results.append(txt)
    
            # If an exception is raised, print an error message
            except:
                print("Error: Could not resolve subdomain")
        return results

