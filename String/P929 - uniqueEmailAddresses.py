class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        seen = set()
        for em in emails:
            local,domain = em.split("@")
            local = local.split("+")[0].replace(".","")
            seen.add(local+"@"+domain)
        return len(seen)