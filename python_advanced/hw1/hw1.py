def parse(query: str) -> dict:
    if '?' not in query:
        return {}
    query = query.split('?')[1]
    if not query:
        return {}

    params = query.split('&')
    result = {}
    for param in params:
        key_value = param.split('=')
        if len(key_value) == 2:
            key, value = key_value
            result[key] = value
    return result


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}

    assert parse('') == {}
    assert parse('https://example.com') == {}
    assert parse('https://example.com/page?name=ferret&color=&size=large') == {'name': 'ferret', 'color': '',
                                                                               'size': 'large'}
    assert parse('https://example.com/products?category=electronics&brand=Samsung&price_range=100-500') == {
        'category': 'electronics', 'brand': 'Samsung', 'price_range': '100-500'}
    assert parse('https://example.com/page?name=&age=28') == {'name': '', 'age': '28'}


def parse_cookie(query: str) -> dict:
    if not query:
        return {}
    cookies = query.rstrip(';').split(';')
    result = {}
    for cookie in cookies:
        key_value = cookie.split('=', 1)
        if len(key_value) == 2:
            key, value = key_value
            result[key.strip()] = value
    return result


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}

    assert parse_cookie('name=;age=28;') == {'name': '', 'age': '28'}
    assert parse_cookie(' name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=;age=28;key=;') == {'name': '', 'age': '28', 'key': ''}
    assert parse_cookie('name=Dima;age=;;key=;') == {'name': 'Dima', 'age': '', 'key': ''}
    assert parse_cookie('user_id=257;username=vasilij;session=private') == {'user_id': '257',
                                                                                  'username': 'vasilij',
                                                                                  'session': 'private'}

