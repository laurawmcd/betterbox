---
layout: default
title: Blog
ref: blog
---

<!-- List of Categories -->
<div class="categories-list">
  <h2>Suits:</h2>
  <ul>
    {% assign all_categories = site.posts | map: 'categories' | join: ',' | split: ',' | uniq %}
    {% for category in all_categories %}
      <li><a href="#{{ category | slugify }}">{{ category }}</a></li>
    {% endfor %}
  </ul>
</div>

<!-- Blog Posts -->
<div class="blog-posts">
  {% for post in site.posts %}
    <h2 id="{{ post.categories | first | slugify }}"><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h2>
    <p class="post-meta">{{ post.date | date: "%B %d, %Y" }}</p>

    <!-- Display Categories -->
    {% if post.categories %}
      <h3>Categories: {{ post.categories | join: ', ' }}</h3>
    {% endif %}

    <p>{{ post.excerpt }}</p>
  {% endfor %}
</div>
