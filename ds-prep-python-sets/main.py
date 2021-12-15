trail_mix = {'m&ms', 'peanuts','raisins'}
print(trail_mix)
print('cashews' in trail_mix)
print('peanuts' in trail_mix)
trail_mix.add('pretzels')
new = {"peanuts", "banana chips", "bits of jerky"}
trail_mix.update(new)
print(trail_mix)
trail_mix.remove('m&ms')
trail_mix.discard('raisins')
trail_mix.discard('rat poison')
print(trail_mix)
nuts = {"peanuts", "cashews", "almonds", "walnuts", "pecans"}
print(trail_mix.union(nuts))
print(nuts.intersection(trail_mix))
print(trail_mix.difference(nuts))
print(nuts.difference(trail_mix))
