import requests
import pygal
from pygal.style import  LightColorizedStyle as LCS, LightenStyle as LS

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code: ", r.status_code)
# ^ tells us whether the request was successful 

# Store API response in a variable
response_dict = r.json()
# print("Total repos: ", response_dict["total_count"])

# # Process results.
# print(response_dict.keys())

repo_dicts = response_dict["items"]
# print("Repos returned: ", len(repo_dicts))


# Examine the first repository
# repo_dict = repo_dicts[0]
# print("\nKeys: ", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

# print("\nSelected information about each repository")
# for repo_dict in repo_dicts:
#     print("Name", repo_dict["name"])
#     print('Owner:', repo_dict['owner']['login'])
#     print('Stars:', repo_dict['stargazers_count'])
#     print('Repository:', repo_dict['html_url'])
#     print('Created:', repo_dict['created_at'])
#     print('Updated:', repo_dict['updated_at'])
#     print('Description:', repo_dict['description'])
    # print()

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    
    plot_dict = {
        'value':repo_dict['stargazers_count'],
        'label':repo_dict['description'] or '',
        'xlink': repo_dict['html_url']
        }
    plot_dicts.append(plot_dict)

# Make a visualization
my_style = LS('#333366', base_style = LCS, major_label_font_size = 18)
# major_label_font_size -> the size of labels on y-axis that mark off increments of 5000 stars

#Making customizations
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
# ^ the size of labels in both x and y axis
my_config.truncate_label = 15
# ^ shorten long proj names
my_config.show_y_guides = False
# ^ hide the horizontal lines
my_config.width = 1000

chart = pygal.Bar(my_config, style = my_style)
chart.title = 'Python Projects on GitHub by the Top # of Stars'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos_github.svg')