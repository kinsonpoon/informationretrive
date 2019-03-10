from SolrClient import SolrClient

while True:
    query = input("Query: ")

    # Preprocessing
    # The query should be "How+do+you+do"
    # Instead of "How do you do"
    query = query.replace(" ", "+")

    # Target solr collection
    solr = SolrClient('http://127.0.0.1:8983/solr')

    res = solr.query('hello_solr', {
        "q": 'question:' + query,
        "indent": "on",
        "rows": "10",
        "wt": "json"}
    )

    # Print the answer field of the most relevent response
    # Most relevent   = res.docs[0]
    # Second relevent = res.docs[1]
    # ...
    # And so on
    print(''.join(res.docs[0]['answer']))
