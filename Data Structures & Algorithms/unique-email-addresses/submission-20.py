class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailSet = set()

        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            emailSet.add(local + "@" + domain)
        return len(emailSet)

