languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

print('\n'.join(['{} was created by {}'.format(k, v)
      for k, v in languages.items()]))

# for k, v in languages.items():
#     print('{} was created by {}'.format(k, v))
