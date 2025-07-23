def get_links(query: str):
    query = query.lower()
    links = []

    if "jee" in query:
        links.append("https://www.mathongo.com/jee-main")
        links.append("https://www.mathongo.com/jee-advanced")

    if "neet" in query:
        links.append("https://www.mathongo.com/neet")

    if "syllabus" in query:
        links.append("https://www.mathongo.com/jee-main/syllabus")
        links.append("https://www.mathongo.com/neet/syllabus")

    if "pattern" in query:
        links.append("https://www.mathongo.com/blog/jee-main-exam-pattern")

    if "form" in query or "deadline" in query:
        links.append("https://www.mathongo.com/blog/jee-form-dates")
        links.append("https://www.mathongo.com/blog/neet-form-dates")

    return links
