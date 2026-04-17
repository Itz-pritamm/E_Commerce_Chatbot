def router(query):
    query = query.lower()

    faq_keywords = [
        "return", "refund", "track", "order",
        "payment", "credit", "debit",
        "offer", "discount"
    ]

    sql_keywords = [
        "buy", "price", "shoes", "nike", "puma",
        "under", "cheap", "size", "rating"
    ]

    if any(word in query for word in faq_keywords):
        return type("obj", (object,), {"name": "faq"})

    if any(word in query for word in sql_keywords):
        return type("obj", (object,), {"name": "sql"})

    return type("obj", (object,), {"name": "faq"})
