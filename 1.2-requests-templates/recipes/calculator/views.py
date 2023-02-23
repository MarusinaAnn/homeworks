from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def recipes_view(request, name):
    if name in DATA:
        data = DATA[name]
        servings = int(request.GET.get('servings', 1))
        if servings != 1:
            result = dict()
            for ingredient, amount in data.items():
                new_value = amount * servings
                result[ingredient] = new_value
            context = {
                'name': name,
                'recipe': result
            }
        else:
            context = {
                'name': name,
                'recipe': data
            }

    else:
        context = None
    return render(request, template_name='calculator/index.html', context=context)


def all_view(request):
    all_recipes = list(DATA.keys())
    context = {'all_recipes': all_recipes}
    return render(request, template_name='calculator/all.html', context=context)

   
# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
