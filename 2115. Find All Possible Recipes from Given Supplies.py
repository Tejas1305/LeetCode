class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        graph = defaultdict(list)
        in_degree = {recipe: 0 for recipe in recipes}

        for recipe, ingredient_list in zip(recipes, ingredients):
            in_degree[recipe] = len(ingredient_list)
            for ing in ingredient_list:
                graph[ing].append(recipe)

        queue = deque(supplies)
        possible_recipes = set(supplies)
        result = []

        while queue:
            item = queue.popleft()

            if item in in_degree:
                result.append(item)

            for recipe in graph[item]:
                in_degree[recipe] -= 1 
                if in_degree[recipe] == 0:
                    queue.append(recipe)

        return result