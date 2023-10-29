---
layout: default
title: Virtual cards
ref: blog
---

<!-- List of Categories: Suits -->
<div class="categories-list">
  <h2>Suits:</h2>
  <ul>
    {% for post in site.categories['Suits'] %}
      <li><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
</div>

<!-- List of Categories: Virtual Cards -->
<div class="categories-list">
  <h2>Virtual Cards:</h2>
  <ul>
    {% for post in site.categories['Virtual Cards'] %}
      <li><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
</div>

<!-- Blog Posts with 50-word Snippets for All Categories -->
<div class="blog-posts">
  {% for category in site.categories %}
    <h3>{{ category[0] }}:</h3>
    <ul>
      {% for post in category[1] %}
        <li>
          <h4><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h4>
          <p>{{ post.content | strip_html | truncatewords:50 }}</p>
        </li>
      {% endfor %}
    </ul>
  {% endfor %}
</div>
