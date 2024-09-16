source "https://rubygems.org"

# Specify the Jekyll version used by GitHub Pages
gem "jekyll", "~> 3.9.3"

# Theme for your Jekyll site
gem "jekyll-theme-cayman-blog"

# GitHub Pages gem with pinned version to match GitHub Pages
gem "github-pages", "~> 228", group: :jekyll_plugins

# Jekyll plugins
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.15.1"
  gem "jekyll-seo-tag", "~> 2.8.0"
  gem "jekyll-sitemap", "~> 1.4.0"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", platforms: [:mingw, :x64_mingw, :mswin]

# Lock `http_parser.rb` gem to `v0.6.x` on JRuby builds
gem "http_parser.rb", "~> 0.6.0", platforms: [:jruby]

# Webrick is not bundled with Ruby 3.0+, so we need to add it explicitly
gem "webrick", "~> 1.8"
