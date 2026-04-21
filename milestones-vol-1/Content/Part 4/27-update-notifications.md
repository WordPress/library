## 27. Update notifications

Peter Westwood became a core committer in July 2007, bringing the number of people who could commit code to four. Westi got involved in the project in 2004 while working as a software engineer -- he had written a script that downloaded WordPress and installed it on a server. He helped with the Codex, and found and fixed bugs. Like many other developers, he had little PHP experience when he came to the project.

The wp-hackers mailing list was in its third year, but productive discussion there diminished over time. More and more decision-making happened elsewhere. For example, in February 2007, <a href="https://core.trac.wordpress.org/ticket/3862">Ryan integrated phpmailer with WordPress</a>. The code was committed after a short discussion on trac. It wasn’t until September that a <a href="http://lists.wordpress.org/pipermail/wp-hackers/2007-September/014497.html">phpmailer conversation took place on wp-hackers</a> -- one that few committers participated in.

Exchanges on the mailing list inclined less toward development, and more toward <a href="http://lists.wordpress.org/pipermail/wp-hackers/2007-September/015058.html">meta-discussions about the mailing list itself</a>, from the <a href="http://lists.wordpress.org/pipermail/wp-hackers/2007-September/015173.html">high signal-to-noise ratio</a>, to <a href="http://lists.wordpress.org/pipermail/wp-hackers/2007-October/015489.html">ideas to improve mailing list etiquette</a>. 	

<a href="http://andy.wordpress.com/2007/10/03/wp-hackers/">Andy Skelton wrote about the problem with wp-hackers</a>:

<blockquote>There is just one thing I want to make clear about wp-hackers: a hacker is not someone who discusses or pays lip service or dissents or casts a vote or says what can or should be done. Hackers aren’t committee members. Hackers are more interested in proving what can be done than arguing about it.</blockquote>

There was too much talking and not enough hacking on wp-hackers, and opinion often swayed conversations rather than fact. Mailing lists can become dominated by people who have time to comment, rather than those doing the work. The latter might have the most valuable feedback, but they’re often too busy to keep up with a high-traffic mailing list. 

WordPress isn’t alone in this phenomenon. A <a href="http://sback.it/publications/msr2013.pdf">2013 study of the Apache Lucene mailing list</a> (PDF) found that “although the declared intent of development mailing list communication is to discuss project internals and code changes/additions, only 35 percent of the email threads regard the implementation of code artefacts.” As well as discussing development, mailing list participants discussed social norms and behavior. The study also found that project developers participate in less than 75 percent of the discussions, and start only half of them. Developers prefer to communicate on the issue-tracking software -- a finding resonant with WordPress, as developers ultimately switched from the mailing list to WordPress trac. 	

Mailing lists tend toward bike shed discussions, [^Fn-1] a term derived from <a href="https://en.wikipedia.org/wiki/Parkinson%27s_law_of_triviality">Parkinson’s law of triviality</a>:	

<blockquote>Parkinson shows how you can go in to the board of directors and get approval for building a multi-million or even billion dollar atomic power plant, but if you want to build a bike shed you will be tangled up in endless discussions.</blockquote>

An atomic plant is so vast that only very few people can grasp it. The board of directors assume that somebody has the knowledge and has done the groundwork. In contrast, everyone can build a bike shed, so everyone has an opinion on how it should be done, and especially what color it should be painted.

In his book <em>Producing Open Source Software</em>, Karl Fogel notes that as the technical difficulty of an issue goes down, the “<a href="http://producingoss.com/en/producingoss.html#bikeshed">probability of meandering goes up</a>:”

<blockquote>...consensus is hardest to achieve in technical questions that are simple to understand and easy to have an opinion about, and in "soft" topics such as organization, publicity, funding, etc. People can participate in those arguments forever, because there are no qualifications necessary for doing so, no clear ways to decide (even afterward) if a decision was right or wrong, and because simply outwaiting other discussants is sometimes a successful tactic.</blockquote>

With its community growth and low barrier to entry, the WordPress project has been susceptible to bike shed discussions like any other free software project. A <a href="https://www.google.com/search?q=site%3Ahttp%3A%2F%2Flists.wordpress.org%2Fpipermail%2Fwp-hackers%2F+bikeshed&amp;oq=site%3A&amp;aqs=chrome.2.69i57j69i58j69i59j69i65l3.2535j0j4&amp;sourceid=chrome&amp;es_sm=91&amp;ie=UTF-8#safe=strict&amp;q=site:http:%2F%2Flists.automattic.com%2Fpipermail%2Fwp-hackers%2F+bikeshed">Google search for “bikeshed” on the wp-hackers mailing list</a> displays the discussions in which someone has cried “bike shed,” as does a <a href="https://core.trac.wordpress.org/search?q=bikeshed&amp;noquickjump=1&amp;changeset=on&amp;ticket=on">similar search on trac</a>.	

In 2007, for example, discussion about what to call links got heated. A <a href="http://lists.wordpress.org/pipermail/wp-hackers/2007-June/013299.html">member of wp-hackers asked</a>, “Anyone know why it's still called Blogroll in admin, when it's called Bookmarks in functions (wp_list_bookmarks) and yet displays by default as a list of "Links" in the sidebar?” The original post, "Blogroll, Bookmarks, Links," generated a total of 79 emails on the mailing list alone, and the discussion spilled <a href="https://core.trac.wordpress.org/ticket/3695">over to a trac ticket</a>.	

Of course, one person’s bike shed is another person’s bête noire, and there were times when wp-hackers was alight with community members who insisted on giving specific issues serious consideration. One such instance was in early September 2007, before the release of WordPress 2.3, which contained the update notification system. This system alerts users when a new version of WordPress or of a plugin becomes available to install. <a href="https://core.trac.wordpress.org/ticket/1476">The system</a> collects information about the WordPress version, PHP version, locale setting, and the website’s URL from a user’s site, and sends it back to http://api.wordpress.org. A <a href="https://core.trac.wordpress.org/changeset/5913">further piece of code</a> carries a <a href="https://core.trac.wordpress.org/ticket/4795">plugin update check</a>, which sends the website’s URL, WordPress version, and plugin info (including inactive plugins) to api.wordpress.org.

For some, the data collection appeared contrary to the free software project ethos. They thought that <a href="http://lists.wordpress.org/pipermail/wp-hackers/2007-September/014860.html">collecting the blog URL was unnecessary</a>. A ticket on WordPress trac <a href="https://core.trac.wordpress.org/ticket/5066">requested that update checking be anonymized</a>. Others had no problem with WordPress collecting the data, but were <a href="http://lists.wordpress.org/pipermail/wp-hackers/2007-September/014919.html">unhappy that WordPress did not disclose it</a>. A number of people who didn’t oppose the changes nevertheless felt that there should be a way to opt out, so that users who required complete privacy would be able to turn off data collection.

This debate goes to the heart of one of WordPress' design philosophies: <em>decisions, not options</em>. This idea is heavily influenced by a <a href="http://ometer.com/free-software-ui.html">2002 article written by GNOME contributor Havoc Pennington</a>. Many free software user interfaces cram in options so that they can be configured in multiple ways. If an argument ensues in a software project about whether something should or shouldn’t be added, a superficial solution is to add an option. The more options one adds, the more unwieldy a user interface becomes. Pennington writes, "preferences have a cost [..], each one has a price and you have to consider its value.” He outlines the problem with too many options:

<ul>
<li>When there are too many preferences it’s difficult for a user to find them.</li>
<li>They can damage QA and testing. Some bugs only happen when a certain configuration of options is selected.</li>
<li>They make creating a good UI difficult.</li>
<li>They keep people from fixing real bugs.</li>
<li>They can confuse users.</li>
<li>The space that you have for preferences is finite so fill it wisely.</li>
</ul>

WordPress developers carefully consider the introduction of any new option, and have become better at it over time. When the data collection question arose, they were extremely reluctant to introduce new options. <a href="http://lists.wordpress.org/pipermail/wp-hackers/2007-September/015119.html">Westi posted to wp-hackers</a>:	

<blockquote>One of the core design ideas for WordPress is that we don't introduce options lightly. The moment you think of making a feature optional you challenge the argument for introducing the feature in the beginning.</blockquote>

What benefit would an opt-out button for update notifications provide to users? The purpose of the notifications is to help users to stay up-to-date and secure. Adding an option to opt out of update notifications would only reduce the number of people who updated their sites, and increase the number of insecure instances of WordPress. The benefit to adding the option didn’t outweigh the cost. 

Consequently, and despite the extensive discussion on wp-hackers, <a href="http://wordpress.org/news/2007/09/wordpress-23/">WordPress 2.3 was launched as planned</a>, with the following note in the announcement post:	

<blockquote>Our new update notification lets you know when there is a new release of WordPress or when any of the plugins you use has an update available. It works by sending your blog URL, plugins, and version information to our new api.wordpress.org service which then compares it to the plugin database and tells you whats (sic) the latest and greatest you can use.</blockquote>

The project also published the <a href="http://lists.wordpress.org/pipermail/wp-hackers/2007-September/015014.html">first version of a privacy policy on WordPress.org</a>.	

Amid these discussions, the project structure changed when <a href="https://wordpress.org/news/2007/09/new-faces/">Peter Westwood and Mark Jaquith became lead developers</a>. The announcement post describes them as “a few old faces who are taking on bigger roles in the community.” Both were active committers who had taken on greater leadership roles. Both had participated in many of the more challenging discussions in the community, and they didn't always agree with current project leadership. They both, for example, opposed Matt’s proposal for the taxonomy structure, and Mark was one of the people who voiced concerns over data collection in WordPress 2.3. They added new perspectives to the project leadership: for the first time since the early days of the project, there were people other than Matt and Ryan to help guide and shape development of both the software and the project.


[^Fn-1] The notion of a bike shed was popularized in FOSS projects by Karl Fogel. In his book, <em><a href="http://producingoss.com/">Producing Open Source Software</a></em>, he reprints <a href="http://bikeshed.com/">an email from Poul-Henning Kamp</a> to the FreeBSD mailing list with the title “A bike shed (any color will do) on greener grass…,” in which Kamp uses the “painting the bikeshed” analogy to describe discussions on the mailing list.
