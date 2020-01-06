# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.elems = []
        for x in range(bucket_count):
            self.elems.append([])

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def does_string_exist(self, h, s):
        for string in self.elems[h]:
            if string == s:
                return True
        return False

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            l = len(self.elems[query.ind])
            self.write_chain(reversed(self.elems[query.ind]))

        else:
            seq = query.s
            h = self._hash_func(seq)
            string_exists = self.does_string_exist(h,seq)

            if query.type == 'find':
                self.write_search_result(string_exists)

            elif query.type == 'add':
                if not string_exists:
                    self.elems[h].append(seq)
            else:
                if string_exists:
                    self.elems[h].remove(seq)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
