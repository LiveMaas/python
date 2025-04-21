#dictionaries

d = {
    'key1' : '123',
    'key2' : '12,23,33',
    'key3' : ['item0','item1','item2']
}
d['key1'] = d['key1'] + 100


d = {'key1':123,
     'key2':[12,23,33],
     'key3':['item0','item1','item2']}

d['key2'].append('apple')
type(d['key1'])

#nested dictionaries
d = {'key1' : {'nestkey' : 'apple'}}

d['key1']
type(d['key1'])
d['key1']['nestkey']
d['key1']['nestkey'][0].upper()

#get inner value
d = {'key1' : {'nestkey' : {'inner_key' : ['inner_value']} } }
d['key1']['nestkey']['inner_key'][0]

#task: get 'hello'
e = {'k1':[{'nest_key':['this is deep',['hello']]}]}
e['k1']
type(e['k1'])
e['k1'][0]['nest_key'][1]
type(e['k1'][0]['nest_key'][1])
e['k1'][0]['nest_key'][1][0]

# task: get hello
f = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
f['k1']
type(f['k1'])
f['k1'][2]
f['k1'][2]['k2'][1]
f['k1'][2]['k2'][1]['tough'][2][0]