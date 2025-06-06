def is_phishing(url):
    suspicious = ["@", "-", "bit.ly", "tinyurl", "//"]
    score = sum(s in url for s in suspicious)
    return score >= 2