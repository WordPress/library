# Building Blocks: The Evolution of WordPress 
## Chapter 12 — WordPress Matures

2019’s theme for WordPress.org was “Tighten Up.” One step forward was the release of [Betty](https://wordpress.org/news/2019/02/betty/), led by [Matt Mullenweg](http://ma.tt/) and [Gary Pendergast](https://pento.net/). It improved editor performance, optimized background processes, and helped users update outdated versions of PHP, and this suite of improvements proved a boon for the Project’s most technical users.

5.1 also introduced several Site Health features. The Site Health project provides a dashboard showing technical issues affecting the health of a website, with suggestions for improvement. Some suggestions are straightforward, like “Delete unused plugins,” but many are intended for developers rather than site owners.

The updates specifically relating to PHP included: 
* Detection of outdated or insecure versions of PHP
* Notices about PHP versions
* Checks for plugin compatibility with the site’s PHP version

[5.2, Jaco](https://wordpress.org/news/2019/05/jaco/), was also released in 2019. It was led by [Matt Mullenweg](http://ma.tt/), [Josepha Haden Chomphosy](https://josepha.blog/), and [Gary Pendergast](https://pento.net/). 

As of 5.2, PHP version 5.6.20 became the minimum version supported by WordPress. 7.3 was recommended. 

![](https://i0.wp.com/wordpress.org/news/files/2019/11/5.3-album-cover.png?w=1440&ssl=1)

The third update for 2019 was [5.3, Kirk](https://wordpress.org/news/2019/11/kirk/), led by [Matt Mullenweg](https://ma.tt/), [Francesca Marano](https://profiles.wordpress.org/francina/), and [David Baumwald](https://profiles.wordpress.org/davidbaumwald). It included a new default theme, Twenty Twenty, designed for the block editor, further tweaks to the Site Health features, and full support for PHP 7.4.

![](https://i0.wp.com/themes.svn.wordpress.org/twentytwenty/2.2/screenshot.png?w=1144&strip=all)

### The importance of PHP updates
WordPress has the democratization of publishing as a central goal: making it easier for more people to share their content online, regardless of their technical skill and knowledge levels. Many happy WordPress users could manage their websites with no knowledge even of HTML or CSS, let alone PHP.


PHP is an open source server-side scripting language that has been used for web development since 1993. Like most computer languages, it gets updated regularly. In the case of PHP, the planned life span is two years from its first stable release. Using old PHP versions is possible, but it has consequences for speed and security.


However, WordPress powers nearly half of the websites around the world. While the WordPress community has a strong streak of independence, allowing WordPress sites to run on outdated, insecure technology would have far-reaching consequences for the internet. 


By 2019, the PHP 5 family was already two years past its end-of-life. Updates had become essential. While it would have been possible to continue to run websites on outdated versions of PHP — and [statistics](https://w3techs.com/technologies/details/pl-php) show that many still do — the tightening up process focused on getting site owners and hosting companies to make those PHP updates.

### The Site Health Project
The Site Health screen in the WordPress admin area gives users information on the version of PHP their site was running, what needs to be updated, and some other recommendations regarding performance and security.

Users of WordPress with lower levels of tech savvy often remain unaware of the changes. PHP updates can be done automatically through many hosting companies, but not without risks. In fact, many site owners found that their websites broke when they updated their PHP version. Sadly, plain white screens and unrecoverable websites were not an uncommon occurrence at that time. 

A widget encouraging users to update had been shown in the dashboards of websites, and sites that were kept up to date could benefit from the White Screen of Death Protection feature introduced in 5.1. Unfortunately, the most vulnerable websites were often the same sites that were not kept up to date and whose users didn’t visit the admin area often enough to see the informative widget. 

Often, the source of the problem was the website’s theme or key plugins. Compatibility problems meant that the themes or plugins could not be used until and unless they were updated to be compatible with the new versions of PHP. While this could be a simple matter for a personal blog — just change the theme and replace the plugins! — it could be a big, costly problem for businesses and organizations relying on their websites. Often, trying to fix the site without downtime or major design changes was the goal, and the Site Health screen was an important tool.


The Site Health Project gave users tips like “Your PHP version should be updated” and “One or more recommended modules are missing.” Unfortunately, many site owners simply had no idea what these instructions meant or how they could fix these problems. 


While there are explanations on the site health screen, they often are couched in terms that many site owners do not understand. For example, here is the explanation for “Not all recommended security headers are installed” from one website:


“Your website does not send all recommended security headers.

* 	Upgrade Insecure Requests
* 	X-XSS protection
* 	X-Content Type Options
* 	Referrer-Policy
* 	Expect-CT
* 	X-Frame-Options
* 	Permissions-Policy
* 	HTTP Strict Transport Security”
	
While this is plenty of information for developers, a small business owner with a WordPress website may have no clue to the meanings of any of those phrases, let alone the actions required to resolve them.
 
The information was written for hosting companies, developers, and other specific audiences, not for every user of WordPress. In some ways, the frustration people felt on encountering this was a symptom of the empowerment WordPress offered. 

Just as medical patients now have access to radiology reports written for medical professionals that may not convey much to patients, site owners had access to health reports for their websites written for specialists. In many cases, they did not convey much to the site owners.

### Responsibility

There have been many conversations in the WordPress community on the question of who should be responsible for WordPress websites. Should there be automatic updates of themes or plugins initiated by the core software? Should WordPress be disabled on an abandoned website, and if so, who gets to decide what constitutes an abandoned website? 


[Aaron Campbell](https://profiles.wordpress.org/aaroncampbell/) pointed out that any decision-making on site ownership and control issues by [WordPress.org](https://wordpress.org/) would end up being decision-making for a large number of people by a small number of people. “Right and wrong,” he said, “is left up to the marketplace.”


On the other hand, the need to update PHP versions is based on security and the health of the internet as a whole. The tightening up in 2019 versions of WordPress aimed at encouraging those updates without forcing them. 


But that was along a continuum from WordPress.org responsibility to individual site owner responsibility. As always, that continuum had a lot more stops along the way. 


Hosting companies stopped supporting old versions of PHP, forcing updates. However, they didn’t always alert site owners that their websites might break—or even that they had broken. Hands-off site owners might not realize that their websites were no longer functional until they began to affect the bottom line of their business or organization, which was when they were in crisis mode. 


One example is the experience of Operation Sail, or [OpSail](https://opsail.org/), a nonprofit established in 1961 by President Kennedy and supported by the U.S. Congress and the British royal family. Their website broke. Months later, as the organization prepared  for an event, they discovered that their website was offline. Neither their hosting company nor the agency that originally built the site was able to solve the problem, and OpSail had to start over.


Agencies and freelance site builders might have a continuing relationship with the site owners, but in many cases, they had only built the site. Without being hired to serve as webmasters, they often did not feel a responsibility to keep these websites functional. 


Many designers do not offer continuing services for the websites they design. Site owners may not even have contact information for the people who built their websites. 


Office staff, who may be users of a website without being owners, may not have any design or development training. They may have limited access and may not even be administrators on a website, even if they are the primary user of the admin area.


While it is possible to imagine further steps that could have been taken to limit the disruption, it is by no means clear who should or could have taken those steps.


The PHP updates were, however, necessary. While many individual users had negative experiences, the changes did not affect the market share or progress of WordPress. 

