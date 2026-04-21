

## 22. Speeding up the Release Cycle

Shuttle wasn’t the only piece of the project that dragged. More than a year elapsed between Shuttle-inspired WordPress 2.0 and the next version, WordPress 2.1. <a href="http://ma.tt/2010/11/one-point-oh/">Matt describes</a> the period as “a dark time in WordPress development history, a lost year.” It was time for a streamlined development process.

WordPress' approach to new versions gives each major release two numbers: 1.5, 2.0, 2.9, 3.4, 4.0. Patch releases get an additional decimal point (2.0.1, for example). Many other software projects, like Drupal, give each major release a round number; over a period of years, the version number climbs. Decimalization avoids that, although it took WordPress a while to settle on regular numbering.

The release cycle was sporadic in the early days. Version numbers jumped haphazardly. Some releases arrived in a few months, while 265 days went by between 1.2 and 1.5 -- the codebase had so many changes that WordPress skipped the interim version numbers, <a href="http://wordpress.org/news/2004/12/version-skip/">going straight from 1.2 to 1.5</a>. Version 1.6 was inflated to 2.0, because of the number of features in it and because 314 days had elapsed between the releases. But the delay between 2.0 (released December 31, 2005) and 2.1 (released January 22, 2007) was the longest to date.  

The mailing list was active, and more developers than ever were attracted to the project. WordPress had been downloaded 1.5 million times. But despite active conversation, no one was shipping code. The <a href="http://wordpress.org/news/2007/01/ella-21/">release post for WordPress 2.1, with its plethora of new features</a>, demonstrated the constant desire to slip in one more feature, rather than waiting to include it in the next release. Feature-packed releases brought myriad improvements, but at a cost: delay.

The delay frustrated contributors because of long release cycles, and because commit access was still restricted to Matt and Ryan. Each free software project approaches commit access differently, and WordPress has a mixture of people who support a controlled, Linux-style commit policy, and those favoring open access. For many developers, the restrictive commit policy was partly to blame for delays. 

Ryan argued that <a href="http://lists.wordpress.org/pipermail/wp-hackers/2006-March/005192.html">a defined funnel</a> avoided situations in which “bridge-burning arguments happen in the repository rather than in ticket comments." When committers are limited, approach and implementation discussions take place before any code touches the main repository, where it’s difficult to remove. An open commit policy makes development more agile, but "loose control leads to spaghetti code and flame wars over inconsequential issues," claimed Douglas Daulton, <a href="http://lists.wordpress.org/pipermail/wp-hackers/2006-March/005195.html">a supporter of the funnel</a>, in a wp-hackers post.

In the context of these discussions, Ryan <a href="http://lists.wordpress.org/pipermail/wp-hackers/2006-March/005190.html">codified a commit process that remains part of development today</a>:

<ul>
<li>Every commit must be accompanied by a ticket.</li>
<li>Before being committed, the code is reviewed by at least two people -- one for a code review and the other for an integration/architecture review.</li>
<li>These reviews are carried out by trusted contributors.</li>
</ul>

By March, 2006, incremental, positive changes were evident. Ryan proposed a focused #wordpress-dev IRC channel as a complement to the #wordpress channel, which had become a place for general chatter and support. Mark Jaquith <a href="http://lists.wordpress.org/pipermail/wp-hackers/2006-March/005189.html">pointed to the Bug Gardening scheme's success</a> in opening trac up; extending privileges to “bug gardeners” responsible for triaging tickets distributed the workload and led to "a whole slew of people who are autonomously fixing bugs, submitting  patches, and having them committed." The trac mailing list was another positive change, transforming trac from simple bug-tracking, to a place for focused discussion and curtailing wp-hackers' tendency to wander down conversational rabbit holes. 

As work on WordPress 2.1 went on, Ryan suggested <a href="http://lists.wordpress.org/pipermail/wp-hackers/2006-October/008871.html">getting WordPress 2.0 into Debian stable</a>, the official version of the  Debian open-source operating system. WordPress was already in the testing and unstable distributions, which each contain packages lined up for inclusion in the stable version. To be included in Debian stable, WordPress 2.0 would need to be maintained for three to five years, including backporting security issues to ensure that all previous versions remained stable. Mark Jaquith took on the task of maintaining the WordPress 2.0 branch, and the project committed to maintaining it for three years, until 2010. 

Shortly after he began leading the legacy branch, <a href="https://core.trac.wordpress.org/changeset/4270">Mark Jaquith received commit access</a>. Mark had been involved with WordPress since 2004, coming to the project from Movable Type. In his two years of work he’d made many contributions, including the successful bug gardening scheme. It was a sign that the funnel was starting to broaden, and the beginning of a period when -- slowly but surely -- more committers were added.

Commit access was offered sparingly; it wasn’t given out based on coding expertise or how much work a developer had done. Adding a new committer meant trusting them to uphold the project’s user-first ethos. “It’s not just that you’ve shown a commitment to contributing,” <a href="http://archive.wordpress.org/interviews/2013_07_02_Westwood.html#L122">says Peter Westwood</a> (<a href="http://profiles.wordpress.org/westi">westi</a>), “but you also have shown an understanding of the ethos of the community, their shared beliefs, and their philosophies.”

Adding another committer didn't speed up the development cycle, so the team took a more serious look at the WordPress development process -- or lack thereof. A discussion on <a href="http://lists.wordpress.org/pipermail/wp-hackers/2006-October/008907.html">moving to a 120-day release cycle</a> started on wp-hackers, and Matt shared his thoughts on what a release timeline should look like:	

<blockquote>

<ul>
<li>2 months of crazy fun wild development where anything goes.</li>
<li>1 month of polishing things a little bit, and performance.</li>
<li>Feature freeze.</li>	
<li>1 month of testing, with a public beta release at the beginning.</li></ul>

</blockquote>

The community response was positive. A 120-day structure provided a concrete deadline, and the shorter release cycles  meant that a feature need not hold up a release, as the next version would, in theory, arrive predictably. (In practice, this often depended on what the feature was, who had spearheaded it, and how far along it was). WordPress 2.1 was the first version to ship with a concrete release date for the next version: <a href="http://wordpress.org/news/2007/01/ella-21/">April 23 for WordPress 2.2</a>. 

Publicizing release dates gave the project firm deadlines, which came to be seen as a promise -- a release date promise that users could plan around. The project didn’t quite make the next deadline, but was only a few weeks off; WordPress 2.2 <a href="http://wordpress.org/news/2007/05/wordpress-22/">released on May 16, 2007</a>. 

