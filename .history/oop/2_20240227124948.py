class py_solution:
    def sub_sets(self, ssets):
        return self.subsetsRecur([],sorted(ssets))

    def subsetsRecur(self, current, sset):
        if sset:
            return   