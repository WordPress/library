# Building Blocks: The Evolution of WordPress 
## Chapter 3 — Plugging into Plugins

### The Extensibility of WordPress
One billion downloads. In 2014, 11 years into its existence, WordPress reached this impressive milestone number of plugin downloads. 

The plugin system is a central distinguishing feature of WordPress, allowing people to have website functionality that would otherwise require thousands of dollars of developer time. Plugins are free pieces of software that add functionality to WordPress websites. Most can be used on any website, with virtually any theme, regardless of the design or content. Most can be downloaded for free and uploaded to the websites. Once activated, they provide special functionality, from inserting analytics code to creating special widgets. With plugins, non-technical users could have everything from shopping carts to galleries on their websites, and WordPress began to be much more than a blogging platform.

At the same time, plugins allowed WordPress developers to keep WordPress core to a practical size and level of complexity without limiting creativity. Instead of shoehorning every great feature into the core functionality, they could add myriad plugins to satisfy a wide range of needs and wants.

The plugin repository was launched in 2005 as a place to host and work on code. Users could browse an alphabetical list of plugins but could not search. With no agreed-upon system for naming plugins, it was impossible to predict what a particular plugin or type of plugin might be named. The repository quickly grew unwieldy.

The plugin directory, a place for users to find the plugins they needed, was launched in 2007. The directory finally made it possible to search for a specific plugin or type.

Plugin update notifications were implemented later that year. In 2008, WordPress admin began offering a simple option for adding plugins without using file transfer protocol, the special software for transferring computer files. This was a boon for non-technical users. 

### A Plugin Explosion
As plugins became more important, the numbers increased significantly. There are — at the time of writing —  [over 60,000 plugins](https://wordpress.org/plugins/). The number doubled from 30,000 in 2014. Almost anything users might want to do with a website could be done with a plugin – if they had the patience to browse through the list and try out enough examples to identify a plugin that would meet their needs. 

At the same time, the sheer number of plugins began to be overwhelming. WordCamp sessions comparing half a dozen social sharing plugins or listing the ten most important plugins became popular. Debates on the correct number of plugins for a single website were common. 

Plugin quality was a concern. Incompatibilities among plugins were (and continue to be) a primary cause of technical issues for WordPress websites.

“I see this entire issue as one of the big problems facing WordPress,” wrote Jeff Chandler at WPTavern. “As more plugins are added to the repository…and the bar to entry to use WordPress is lowered even more, the ingredients are slowly coming together to increase the risk for all who use the software.”

Users wondered why they should sift through dozens of contact form plugins. Couldn’t WordPress include one? The Core team created the idea of identifying core plugins: the best examples of the most important plugins, developed with the same care that went into core WordPress.

The advantages were obvious, but plugin developers balked.

In 2009, a core plugins project was launched…and died.

“There’s a lot of potential with having a more curated list of plugins,” core team member [Aaron Campbell](https://profiles.wordpress.org/aaroncampbell/) suggests. He thought of the often-referenced distinction between the cathedral and the bazaar. Getting everyone to collaborate on one magnificent contact form may seem like a better idea than having the fragmented focus of dozens of similar plugins. 

But there are benefits to the fragmentation, too. “There’s a wide array of users with different needs,” he points out. Each new idea for a contact form may work best in a slightly different setting. “They all have their markets.”

Besides, Aaron asks, who should sift through those 60,000 plugins and identify the best? The WordPress Foundation? A committee? “That’s a lot of weight to put on a small group,” he says. 

Matt says, “WordPress does best when we give people a lot of control.” In his 2022 State of the Word address, he announced a new taxonomy for the plugin directory, allowing plugin developers to self-identify the type of plugins they’re offering: solo or single-player plugins, community plugins, canonical plugins which are supported by WordPress core developers, and commercial plugins which might include upsells and freemium models. This new taxonomy helps users get a clear idea of what is offered with any given plugin. 

### Plugin Security

A plugin repository review team was established in 2012. The group included Mark Riley, Samuel Wood (Otto), Mika Epstein, Pippin Williamson, Boone Gorges, and Scott Riley.

In 2014, when the repository marked its billionth download, the top ten most popular plugins list began with Akismet and WordPress SEO by Yoast. Contact Form 7, Jetpack, and NextGen Gallery were high on the list, along with WooCommerce. 

![](https://wordpress.org/book/files/2023/05/Screenshot-of-WordPress-Featured-Plugins.png)

Akismet, the core plugin that shields WordPress sites from spam comments, had been downloaded 25,653,482 times. 

Custom Contacts Form wasn’t in the top ten that year, but it hit the headlines when Sucuri revealed that the plugin had a vulnerability that allowed the remote takeover of the 600,000+ sites it lived in. 

The WordPress security team worked with the developers to fix the vulnerability and to offer a patch, but Sucuri had already advised readers to jump ship. 

“Due to the unresponsive nature of the development team, we’d encourage you to pursue other sources for your WordPress form needs,” [they wrote](https://blog.sucuri.net/2014/08/database-takeover-in-custom-contact-forms.html). “There are various options with developers that are very responsive and are actively concerned with your security needs. The most common and popular ones would obviously be JetPack [sic] and Gravity Forms.”

2014 was also the year that the WordPress security team discovered 14 malicious plugins that inserted code to hijack websites. The plugins were removed from the repository, but hundreds of sites continued to use the malicious plugins. 

Some community members wanted WordPress to alert everyone who downloaded the plugin. 

"IF an exploit exists and we publicize that fact without a patch, we put you MORE at risk," [said Mika Epstein](https://wordpress.org/ideas/topic/alert-when-installed-plugins-have-been-removed-from-the-plugin-directory/page/2#post-30439), a security team member. "If we make it known there is an exploit, [MOST] hackers attack everyone. If we don't tell anyone, then hackers who DO know will attack, but they would have anyway.”

Other community members proposed that WordPress simply disable and remove the plugins from websites. Practical, legal, and ethical issues made this idea unworkable. 

### Auto Updates

WordPress has a limited ability to force updates, which was added to WordPress in 2013. Aaron, formerly the Security team's representative, explained that a self-hosted WordPress install is designed to check in with WordPress servers. The servers respond with security alerts. This is how WordPress websites tell their owners that updates are needed.

There was [extensive discussion](https://make.wordpress.org/core/2020/11/10/wp5-6-auto-update-implementation-change/) of auto updates during this time. Over the years, increasing the implementation of auto updates in core has become a settled goal for WordPress. In 2013, however, auto updates for minor releases of WordPress core were a new feature of version 3.7. There was controversy, with reactions ranging from relief that updates were easier to the angry insistence that updates should never be automatic for reasons of personal liberty.

WordPress shared [instructions for disabling](https://make.wordpress.org/core/2013/10/25/the-definitive-guide-to-disabling-auto-updates-in-wordpress-3-7/) auto updates and plugins were developed to make it easier. However, Andrew Nacin wrote in his instructions for sabotaging the auto updates, “I’d argue that ‘I don’t want them’ is not a compelling reason for disabling updates. If you don’t keep your site up to date, you are making the web a less safe place for you and everyone who visits your website.”

Site owners got the chance to opt into auto updates for major core versions with 5.6 in 2020.

If core security is involved and the site owner doesn’t take the necessary steps, the WordPress servers will instruct the website to update itself. This is done for core updates but also for some plugins.

Which plugins? There are two factors, Aaron says. First, how bad is the vulnerability? Second, how many sites are using the plugin?

A plugin that would allow remote takeover would cause a severe vulnerability. A plugin that added a pop-up advertisement would not be as severe – but if it had 600,000 downloads, it could affect the ecosystem more severely. Balancing the two factors allows WordPress security to make the decision.

“The Wild West of plugins makes that considerably more challenging,” Aaron points out. 

Core contributor Ian Dunn suggested in a recent discussion that abandoned websites could be candidates for forced updates while frequently updated websites might be treated differently. This discussion included comments like that from core contributor Angelika Reisiger who called on colleagues to “respect the responsibility and the ownership of these webmasters.”

Ian brought the discussion full circle, saying, “Do we let them get hacked and then damage the rest of the Internet, in order to respect their rights; or do we break some of them in order to keep them all secure?”

The philosophical questions linger. Meanwhile, Aaron says, WordPress keeps up with plugin security through defensive coding and relationships with major plugin authors and companies. WordPress stays in close contact with Yoast, Awesome Motive, and makers of other very widely used plugins, ensuring that good communication practices are in place when issues need to be resolved. 
