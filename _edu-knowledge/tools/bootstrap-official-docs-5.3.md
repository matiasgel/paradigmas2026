# Bootstrap official documentation 5.3

- start_url: https://getbootstrap.com/docs/5.3/getting-started/introduction/
- prefix: https://getbootstrap.com/docs/5.3/
- downloaded_at: 2026-04-29T13:46:06.173759+00:00
- pages_saved: 55
- pages_seen: 65
- failures: 0

## Get started with Bootstrap · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/getting-started/introduction/
- fetched_at: 2026-04-29T13:45:45.292819+00:00

View on GitHub
Get started with Bootstrap
Bootstrap is a powerful, feature-packed frontend toolkit. Build anything—from prototype to production—in minutes.
On this page
Quick start
Get started by including Bootstrap’s production-ready CSS and JavaScript via CDN without the need for any build steps. See it in practice with this
Bootstrap CodePen demo
.
Create a new
index.html
file in your project root.
Include the
<meta name="viewport">
tag as well for
proper responsive behavior
in mobile devices.
<!
doctype
html
>
<
html
lang
=
"
en
"
>
<
head
>
<
meta
charset
=
"
utf-8
"
>
<
meta
name
=
"
viewport
"
content
=
"
width=device-width, initial-scale=1
"
>
<
title
>
Bootstrap demo
</
title
>
</
head
>
<
body
>
<
h1
>
Hello, world!
</
h1
>
</
body
>
</
html
>
Include Bootstrap’s CSS and JS.
Place the
<link>
tag in the
<head>
for our CSS, and the
<script>
tag for our JavaScript bundle (including Popper for positioning dropdowns, popovers, and tooltips) before the closing
</body>
. Learn more about our
CDN links
.
<!
doctype
html
>
<
html
lang
=
"
en
"
>
<
head
>
<
meta
charset
=
"
utf-8
"
>
<
meta
name
=
"
viewport
"
content
=
"
width=device-width, initial-scale=1
"
>
<
title
>
Bootstrap demo
</
title
>
<
link
href
=
"
https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css
"
rel
=
"
stylesheet
"
integrity
=
"
sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB
"
crossorigin
=
"
anonymous
"
>
</
head
>
<
body
>
<
h1
>
Hello, world!
</
h1
>
<
script
src
=
"
https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js
"
integrity
=
"
sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI
"
crossorigin
=
"
anonymous
"
>
</
script
>
</
body
>
</
html
>
You can also include
Popper
and our JS separately. If you don’t plan to use dropdowns, popovers, or tooltips, save some kilobytes by not including Popper.
<
script
src
=
"
https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js
"
integrity
=
"
sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r
"
crossorigin
=
"
anonymous
"
>
</
script
>
<
script
src
=
"
https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.min.js
"
integrity
=
"
sha384-G/EV+4j2dNv+tEPo3++6LCgdCROaejBqfUeNjuKAiuXbjrxilcCdDz6ZAVfHWe1Y
"
crossorigin
=
"
anonymous
"
>
</
script
>
Hello, world!
Open the page in your browser of choice to see your Bootstrapped page. Now you can start building with Bootstrap by creating your own
layout
, adding dozens of
components
, and utilizing
our official examples
.
CDN links
As reference, here are our primary CDN links.
Description
URL
CSS
https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css
JS
https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js
You can also use the CDN to fetch any of our
additional builds listed in the Contents page
.
When using CDN links, be sure to use the
integrity
attribute to verify the correct files and versions. These hashes are unique to each file and version of Bootstrap, so when you update to a new version, be sure the
integrity
attribute is also updated.
We also include a
crossorigin="anonymous"
attribute to prevent
CORS
errors.
Next steps
Read a bit more about some
important global environment settings
that Bootstrap utilizes.
Read about what’s included in Bootstrap in our
contents section
and the list of
components that require JavaScript
below.
Need a little more power? Consider building with Bootstrap by
including the source files via package manager
.
Looking to use Bootstrap as a module with
<script type="module">
? Please refer to our
using Bootstrap as a module
section.
JS components
Curious which components explicitly require our JavaScript and Popper? If you’re at all unsure about the general page structure, keep reading for an example page template.
Accordions for extending our Collapse plugin
Alerts for dismissing
Buttons for toggling states and checkbox/radio functionality
Carousel for all slide behaviors, controls, and indicators
Collapse for toggling visibility of content
Dropdowns for displaying and positioning (also requires
Popper
)
Modals for displaying, positioning, and scroll behavior
Navbar for extending our Collapse and Offcanvas plugins to implement responsive behaviors
Navs with the Tab plugin for toggling content panes
Offcanvases for displaying, positioning, and scroll behavior
Scrollspy for scroll behavior and navigation updates
Toasts for displaying and dismissing
Tooltips and popovers for displaying and positioning (also requires
Popper
)
Important globals
Bootstrap employs a handful of important global styles and settings, all of which are almost exclusively geared towards the
normalization
of cross browser styles. Let’s dive in.
HTML5 doctype
Bootstrap requires the use of the HTML5 doctype. Without it, you’ll see some funky and incomplete styling.
<!
doctype
html
>
<
html
lang
=
"
en
"
>
...
</
html
>
Viewport meta
Bootstrap is developed
mobile first
, a strategy in which we optimize code for mobile devices first and then scale up components as necessary using CSS media queries. To ensure proper rendering and touch zooming for all devices, add the responsive viewport meta tag to your
<head>
.
<
meta
name
=
"
viewport
"
content
=
"
width=device-width, initial-scale=1
"
>
You can see an example of this in action in the
quick start
.
Box-sizing
For more straightforward sizing in CSS, we switch the global
box-sizing
value from
content-box
to
border-box
. This ensures
padding
does not affect the final computed width of an element, but it can cause problems with some third-party software like Google Maps and Google Custom Search Engine.
On the rare occasion you need to override it, use something like the following:
.selector-for-some-widget
{
box-sizing
:
content-box
;
}
With the above snippet, nested elements—including generated content via
::before
and
::after
—will all inherit the specified
box-sizing
for that
.selector-for-some-widget
.
Learn more about
box model and sizing at CSS Tricks
.
Reboot
For improved cross-browser rendering, we use
Reboot
to correct inconsistencies across browsers and devices while providing slightly more opinionated resets to common HTML elements.
Community
Stay up-to-date on the development of Bootstrap and reach out to the community with these helpful resources.
Read and subscribe to
The Official Bootstrap Blog
.
Ask questions and explore
our GitHub Discussions
.
Discuss, ask questions, and more on
the community Discord
or
Bootstrap subreddit
.
Chat with fellow Bootstrappers in IRC. On the
irc.libera.chat
server, in the
#bootstrap
channel.
Implementation help may be found at Stack Overflow (tagged
bootstrap-5
).
Developers should use the keyword
bootstrap
on packages that modify or add to the functionality of Bootstrap when distributing through
npm
or similar delivery mechanisms for maximum discoverability.
You can also follow
@getbootstrap on X
for the latest gossip and awesome music videos.


## Examples · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/examples/
- fetched_at: 2026-04-29T13:45:45.466335+00:00

Starters
Functional examples of using Bootstrap in common JS frameworks like Webpack, Parcel, Vite, and more you can edit in StackBlitz.
CDN starter
Instantly include Bootstrap's compiled CSS and JavaScript via the jsDelivr CDN.
Edit in StackBlitz
Sass & JS
Use npm to import and compile Bootstrap's Sass with Autoprefixer and Stylelint, plus our bundled JavaScript.
Edit in StackBlitz
Sass & ESM JS
Import and compile Bootstrap's Sass with Autoprefixer and Stylelint, and compile our source JavaScript with an ESM shim.
Edit in StackBlitz
Bootstrap color modes
Import and compile Bootstrap's Sass with Stylelint, and the Bootstrap color modes.
Edit in StackBlitz
Bootstrap Icons
Import and compile Bootstrap's Sass with Stylelint, PurgeCSS, and the Bootstrap Icons web font.
Edit in StackBlitz
Parcel
Import and bundle Bootstrap's source Sass and JavaScript via Parcel.
Edit in StackBlitz
React
Import and bundle Bootstrap's source Sass and JavaScript with React, Next.js, and React Bootstrap.
Edit in StackBlitz
Vite
Import and bundle Bootstrap's source Sass and JavaScript with Vite.
Edit in StackBlitz
Vue
Import and bundle Bootstrap's source Sass and JavaScript with Vue and Vite.
Edit in StackBlitz
Webpack
Import and bundle Bootstrap's source Sass and JavaScript with Webpack.
Edit in StackBlitz
Snippets
Common patterns for building sites and apps that build on existing components and utilities with custom CSS and more.
Headers
Display your branding, navigation, search, and more with these header components
Heroes
Set the stage on your homepage with heroes that feature clear calls to action.
Features
Explain the features, benefits, or other details in your marketing content.
Sidebars
Common navigation patterns ideal for offcanvas or multi-column layouts.
Footers
Finish every page strong with an awesome footer, big or small.
Dropdowns
Enhance your dropdowns with filters, icons, custom styles, and more.
List groups
Extend list groups with utilities and custom styles for any content.
Modals
Transform modals to serve any purpose, from feature tours to dialogs.
Badges
Make badges work with custom inner HTML and new looks.
Breadcrumbs
Integrate custom icons and create stepper components.
Buttons
Create custom buttons for just about any use case with utilities.
Jumbotrons
Create modernized versions of the classic Bootstrap component.
Custom Components
Brand-new components and templates to help folks quickly get started with Bootstrap and demonstrate best practices for adding onto the framework.
Album
Simple one-page template for photo galleries, portfolios, and more.
Pricing
Example pricing page built with Cards and featuring a custom header and footer.
Checkout
Custom checkout form showing our form components and their validation features.
Product
Lean product-focused marketing page with extensive grid and image work.
Cover
A one-page template for building simple and beautiful home pages.
Carousel
Customize the navbar and carousel, then add some new components.
Blog
Magazine like blog template with header, navigation, featured content.
Dashboard
Basic admin dashboard shell with fixed sidebar and navbar.
Sign-in
Custom form layout and design for a simple sign in form.
Sticky footer
Attach a footer to the bottom of the viewport when page content is short.
Sticky footer navbar
Attach a footer to the bottom of the viewport with a fixed top navbar.
Jumbotron
Use utilities to recreate and enhance Bootstrap 4's jumbotron.
Framework
Examples that focus on implementing uses of built-in components provided by Bootstrap.
Starter template
Nothing but the basics: compiled CSS and JavaScript.
Grid
Multiple examples of grid layouts with all four tiers, nesting, and more.
Cheatsheet
Kitchen sink of Bootstrap components.
Navbars
Taking the default navbar component and showing how it can be moved, placed, and extended.
Navbars
Demonstration of all responsive and container options for the navbar.
Navbars offcanvas
Same as the Navbars example, but with our offcanvas component.
Navbar static
Single navbar example of a static top navbar along with some additional content.
Navbar fixed
Single navbar example with a fixed top navbar along with some additional content.
Navbar bottom
Single navbar example with a bottom navbar along with some additional content.
Offcanvas navbar
Turn your expandable navbar into a sliding offcanvas menu (doesn't use our offcanvas component).
RTL
See Bootstrap's RTL version in action with these modified examples from various categories.
RTL is still experimental
and will evolve with feedback. Spotted something or have an
 improvement to suggest?
Please open an issue.
Album RTL
Simple one-page template for photo galleries, portfolios, and more.
Checkout RTL
Custom checkout form showing our form components and their validation features.
Carousel RTL
Customize the navbar and carousel, then add some new components.
Blog RTL
Magazine like blog template with header, navigation, featured content.
Dashboard RTL
Basic admin dashboard shell with fixed sidebar and navbar.
Cheatsheet RTL
Kitchen sink of Bootstrap components, RTL.
Integrations
Integrations with external libraries.
Masonry
Combine the powers of the Bootstrap grid and the Masonry layout.


## Migrating to v5 · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/migration/
- fetched_at: 2026-04-29T13:45:45.881025+00:00

View on GitHub
Migrating to v5
Track and review changes to the Bootstrap source files, documentation, and components to help you migrate from v4 to v5.
On this page
v5.3.6
Dependencies
Migrated from Hugo to Astro for building our documentation
v5.3.0
If you’re migrating from our previous alpha releases of v5.3.0, please review their changes in addition to this section.
Helpers
Colored links
once again have
!important
so they work better with our newly added link utilities.
Utilities
Added new
.d-inline-grid
display utility
.
v5.3.0-alpha2
If you’re migrating from our previous alpha release of v5.3.0, please review the changes listed below.
CSS variables
Removed several duplicate and unused root CSS variables.
Color modes
Dark mode colors are now derived from our theme colors (e.g.,
$primary
) in Sass, rather than color specific tints or shades (e.g.,
$blue-300
). This allows for a more automated dark mode when customizing the default theme colors.
Added Sass maps for generating theme colors for dark mode text, subtle background, and subtle border.
Snippet examples
are now ready for dark mode with updated markup and reduced custom styles.
Added
color-scheme: dark
to dark mode CSS to change OS level controls like scrollbars
Form validation
border-color
and text
color
states now respond to dark mode, thanks to new Sass and CSS variables.
Dropped recently added form control background CSS variables and reassigned the Sass variables to use CSS variables instead. This simplifies the styling across color modes and avoids an issue where form controls in dark mode wouldn’t update properly.
Our
box-shadow
s will once again always stay dark instead of inverting to white when in dark mode.
Improved HTML and JavaScript for our color mode toggle script. The selector for changing the active SVG has been improved, and the markup made more accessible with ARIA attributes.
Improved docs code syntax colors and more across light and dark modes.
Typography
We no longer set a color for
$headings-color-dark
or
--bs-heading-color
for dark mode. To avoid several problems of headings within components appearing the wrong color, we’ve set the Sass variable to
null
and added a
null
check like we use on the default light mode.
Components
Cards now have a
color
set on them to improve rendering across color modes.
Added new
.nav-underline
variant for our navigation with a simpler bottom border under the active nav link.
See the docs for an example.
Navs now have new
:focus-visible
styles that better match our custom button focus styles.
Helpers
Added new
.icon-link
helper to quickly place and align Bootstrap Icons alongside a textual link. Icon links support our new link utilities, too.
Added new focus ring helper for removing the default
outline
and setting a custom
box-shadow
focus ring.
Utilities
Renamed Sass and CSS variables
${color}-text
to
${color}-text-emphasis
to match their associated utilities.
Added new
.link-body-emphasis
helper alongside our
colored links
. This creates a colored link using our color mode responsive emphasis color.
Added new link utilities for link color opacity, underline offset, underline color, and underline opacity.
Explore the new links utilities.
CSS variable based
border-width
utilities have been reverted to set their property directly (as was done prior to v5.2.0). This avoids inheritance issues across nested elements, including tables.
Added new
.border-black
utility to match our
.text-black
and
.bg-black
utilities.
Deprecated
The
.text-muted
utility and
$text-muted
Sass variable have been deprecated and replaced with
.text-body-secondary
and
$body-secondary-color
.
Docs
Examples are now displayed with the appropriate light or dark color mode as dictated by the setting in our docs. Each example has an individual color mode picker.
Improved included JavaScript for live Toast demo.
Added
twbs/examples
repo contents to the top of the Examples page.
Tooling
Added SCSS testing via True to help test our utilities API and other customizations.
Replaced instances of our bootstrap-npm-starter project with the newer and more complete
twbs/examples repo
.
For a complete list of changes,
see the v5.3.0-alpha2 project on GitHub
.
v5.3.0-alpha1
Color modes!
Learn more by reading the new
color modes documentation
.
Global support for light (default) and dark color modes.
Set color mode globally on the
:root
element, on groups of elements and components with a wrapper class, or directly on components, with
data-bs-theme="light|dark"
. Also included is a new
color-mode()
mixin that can output a ruleset with the
data-bs-theme
selector or a media query, depending on your preference.
Deprecated
Color modes replace dark variants for components, so
.btn-close-white
,
.carousel-dark
,
.dropdown-menu-dark
, and
.navbar-dark
are deprecated.
New extended color system.
We’ve added new theme colors (but not in
$theme-colors
) for a more nuanced, system-wide color palette with new secondary, tertiary, and emphasis colors for
color
and
background-color
. These new colors are available as Sass variables, CSS variables, and utilities.
We’ve also expanded our theme color Sass variables, CSS variables, and utilities to include text emphasis, subtle background colors, and subtle border colors. These are available as Sass variables, CSS variables, and utilities.
Adds new
_variables-dark.scss
stylesheet to house dark-mode specific overrides. This stylesheet should be imported immediately after the existing
_variables.scss
file in your import stack.
diff --git a/scss/bootstrap.scss b/scss/bootstrap.scss
index 8f8296def..449d70487 100644
--- a/scss/bootstrap.scss
+++ b/scss/bootstrap.scss
@@ -6,6 +6,7 @@
// Configuration
@import "functions";
@import "variables";
+
@import "variables-dark";
@import "maps";
@import "mixins";
@import "utilities";
CSS variables
Restores CSS variables for breakpoints, though we don’t use them in our media queries as they’re not supported. However, these can be useful in JS-specific contexts.
Per the color modes update, we’ve added new utilities for new Sass CSS variables
secondary
and
tertiary
text and background colors, plus
{color}-bg-subtle
,
{color}-border-subtle
, and
{color}-text-emphasis
for our theme colors. These new colors are available through Sass and CSS variables (but not our color maps) with the express goal of making it easier to customize across multiple colors modes like light and dark.
Adds additional variables for alerts,
.btn-close
, and
.offcanvas
.
The
--bs-heading-color
variable is back with an update and dark mode support. First, we now check for a
null
value on the associated Sass variable,
$headings-color
, before trying to output the CSS variable, so by default it’s not present in our compiled CSS. Second, we use the CSS variable with a fallback value,
inherit
, allowing the original behavior to persist, but also allowing for overrides.
Converts links to use CSS variables for styling
color
, but not
text-decoration
. Colors are now set with
--bs-link-color-rgb
and
--bs-link-opacity
as
rgba()
color, allowing you to customize the translucency with ease. The
a:hover
pseudo-class now overrides
--bs-link-color-rgb
instead of explicitly setting the
color
property.
--bs-border-width
is now being used in more components for greater control over default global styling.
Adds new root CSS variables for our
box-shadow
s, including
--bs-box-shadow
,
--bs-box-shadow-sm
,
--bs-box-shadow-lg
, and
--bs-box-shadow-inset
.
Components
Alert
Alert variants are now styled via CSS variables.
Deprecated
The
alert-variant()
mixin is now deprecated. We now
use a Sass loop
directly to modify the component’s default CSS variables for each variant.
List group
List group item variants are now styled via CSS variables.
Deprecated
The
list-group-item-variant()
mixin is now deprecated. We now
use a Sass loop
directly to modify the component’s default CSS variables for each variant.
Dropdowns
Deprecated
The
.dropdown-menu-dark
class has been deprecated and replaced with
data-bs-theme="dark"
on the dropdown or any parent element.
See the docs for an example.
Close button
Deprecated
The
.btn-close-white
class has been deprecated and replaced with
data-bs-theme="dark"
on the close button or any parent element.
See the docs for an example.
Navbar
Deprecated
The
.navbar-dark
class has been deprecated and replaced with
data-bs-theme="dark"
on the navbar or any parent element.
See the docs for updated examples.
Progress bars
The markup for
progress bars
has been updated in v5.3.0. Due to the placement of
role
and various
aria-
attributes on the inner
.progress-bar
element,
some screen readers were not announcing zero value progress bars
. Now,
role="progressbar"
and the relevant
aria-*
attributes are on the outer
.progress
element, leaving the
.progress-bar
purely for the visual presentation of the bar and optional label.
While we recommend adopting the new markup for improved compatibility with all screen readers, note that the legacy progress bar structure will continue to work as before.
<!-- Previous markup -->
<
div
class
=
"
progress
"
>
<
div
class
=
"
progress-bar
"
role
=
"
progressbar
"
aria-label
=
"
Basic example
"
style
=
"
width
:
25%
"
aria-valuenow
=
"
25
"
aria-valuemin
=
"
0
"
aria-valuemax
=
"
100
"
>
</
div
>
</
div
>
<!-- New markup -->
<
div
class
=
"
progress
"
role
=
"
progressbar
"
aria-label
=
"
Basic example
"
aria-valuenow
=
"
25
"
aria-valuemin
=
"
0
"
aria-valuemax
=
"
100
"
>
<
div
class
=
"
progress-bar
"
style
=
"
width
:
25%
"
>
</
div
>
</
div
>
We’ve also introduced a new
.progress-stacked
class to more logically wrap
multiple progress bars
into a single stacked progress bar.
<!-- Previous markup -->
<
div
class
=
"
progress
"
>
<
div
class
=
"
progress-bar
"
role
=
"
progressbar
"
aria-label
=
"
Segment one
"
style
=
"
width
:
15%
"
aria-valuenow
=
"
15
"
aria-valuemin
=
"
0
"
aria-valuemax
=
"
100
"
>
</
div
>
<
div
class
=
"
progress-bar bg-success
"
role
=
"
progressbar
"
aria-label
=
"
Segment two
"
style
=
"
width
:
30%
"
aria-valuenow
=
"
30
"
aria-valuemin
=
"
0
"
aria-valuemax
=
"
100
"
>
</
div
>
<
div
class
=
"
progress-bar bg-info
"
role
=
"
progressbar
"
aria-label
=
"
Segment three
"
style
=
"
width
:
20%
"
aria-valuenow
=
"
20
"
aria-valuemin
=
"
0
"
aria-valuemax
=
"
100
"
>
</
div
>
</
div
>
<!-- New markup -->
<
div
class
=
"
progress-stacked
"
>
<
div
class
=
"
progress
"
role
=
"
progressbar
"
aria-label
=
"
Segment one
"
aria-valuenow
=
"
15
"
aria-valuemin
=
"
0
"
aria-valuemax
=
"
100
"
style
=
"
width
:
15%
"
>
<
div
class
=
"
progress-bar
"
>
</
div
>
</
div
>
<
div
class
=
"
progress
"
role
=
"
progressbar
"
aria-label
=
"
Segment two
"
aria-valuenow
=
"
30
"
aria-valuemin
=
"
0
"
aria-valuemax
=
"
100
"
style
=
"
width
:
30%
"
>
<
div
class
=
"
progress-bar bg-success
"
>
</
div
>
</
div
>
<
div
class
=
"
progress
"
role
=
"
progressbar
"
aria-label
=
"
Segment three
"
aria-valuenow
=
"
20
"
aria-valuemin
=
"
0
"
aria-valuemax
=
"
100
"
style
=
"
width
:
20%
"
>
<
div
class
=
"
progress-bar bg-info
"
>
</
div
>
</
div
>
</
div
>
Forms
.form-control
is now styled with CSS variables to support color modes. This includes the addition of two new root CSS variables for the default and disabled form control backgrounds.
.form-check
and
.form-switch
components are now built with CSS variables for setting the
background-image
. The usage here differs from other components in that the various focus, active, etc states for each component aren’t set on the base class. Instead, the states override one variable (e.g.,
--bs-form-switch-bg
).
Floating form labels now have a
background-color
to fix support for
<textarea>
elements. Additional changes have been made to also support disabled states and more.
Fixed display of date and time inputs in WebKit based browsers.
Utilities
Deprecated
.text-muted
will be replaced by
.text-body-secondary
in v6.
With the addition of the expanded theme colors and variables, the
.text-muted
variables and utility have been deprecated with v5.3.0. Its default value has also been reassigned to the new
--bs-secondary-color
CSS variable to better support color modes. It will be removed in v6.0.0.
Adds new
.overflow-x
,
.overflow-y
, and several
.object-fit-*
utilities.
The object-fit property is used to specify how an
<img>
or
<video>
should be resized to fit its container, giving us a responsive alternative to using
background-image
for a resizable fill/fit image.
Adds new
.fw-medium
utility.
Added new
.z-*
utilities
for
z-index
.
Box shadow utilities
(and Sass variables) have been updated for dark mode. They now use
--bs-body-color-rgb
to generate the
rgba()
color values, allowing them to easily adapt to color modes based on the specified foreground color.
For a complete list of changes,
see the v5.3.0 project on GitHub
.
v5.2.0
Refreshed design
Bootstrap v5.2.0 features a subtle design update for a handful of components and properties across the project,
most notably through refined
border-radius
values on buttons and form controls
. Our documentation also has been updated with a new homepage, simpler docs layout that no longer collapses sections of the sidebar, and more prominent examples of
Bootstrap Icons
.
More CSS variables
We’ve updated all our components to use CSS variables.
While Sass still underpins everything, each component has been updated to include CSS variables on the component base classes (e.g.,
.btn
), allowing for more real-time customization of Bootstrap. In subsequent releases, we'll continue to expand our use of CSS variables into our layout, forms, helpers, and utilities. Read more about CSS variables in each component on their respective documentation pages.
Our CSS variable usage will be somewhat incomplete until Bootstrap 6. While we’d love to fully implement these across the board, they do run the risk of causing breaking changes. For example, setting
$alert-border-width: var(--bs-border-width)
in our source code breaks potential Sass in your own code if you were doing
$alert-border-width * 2
for some reason.
As such, wherever possible, we will continue to push towards more CSS variables, but please recognize our implementation may be slightly limited in v5.
New
_maps.scss
Bootstrap v5.2.0 introduced a new Sass file with
_maps.scss
.
It pulls out several Sass maps from
_variables.scss
to fix an issue where updates to an original map were not applied to secondary maps that extend them. For example, updates to
$theme-colors
were not being applied to other theme maps that relied on
$theme-colors
, breaking key customization workflows. In short, Sass has a limitation where once a default variable or map has been
used
, it cannot be updated.
There’s a similar shortcoming with CSS variables when they’re used to compose other CSS variables.
This is why variable customizations in Bootstrap have to come after
@import "functions"
, but before
@import "variables"
and the rest of our import stack. The same applies to Sass maps—you must override the defaults before they get used. The following maps have been moved to the new
_maps.scss
:
$theme-colors-rgb
$utilities-colors
$utilities-text
$utilities-text-colors
$utilities-bg
$utilities-bg-colors
$negative-spacers
$gutters
Your custom Bootstrap CSS builds should now look something like this with a separate maps import.
// Functions come first
@import "functions";
// Optional variable overrides here
+
$custom-color: #df711b;
+
$custom-theme-colors: (
+
"custom": $custom-color
+
);
// Variables come next
@import "variables";
+
// Optional Sass map overrides here
+
$theme-colors: map-merge($theme-colors, $custom-theme-colors);
+
+
// Followed by our default maps
+
@import "maps";
+
// Rest of our imports
@import "mixins";
@import "utilities";
@import "root";
@import "reboot";
// etc
New utilities
Expanded
font-weight
utilities
to include
.fw-semibold
for semibold fonts.
Expanded
border-radius
utilities
to include two new sizes,
.rounded-4
and
.rounded-5
, for more options.
Additional changes
Introduced new
$enable-container-classes
option. —
Now when opting into the experimental CSS Grid layout,
.container-*
classes will still be compiled, unless this option is set to
false
. Containers also now keep their gutter values.
Offcanvas component now has
responsive variations
.
The original
.offcanvas
class remains unchanged—it hides content across all viewports. To make it responsive, change that
.offcanvas
class to any
.offcanvas-{sm|md|lg|xl|xxl}
class.
Thicker table dividers are now opt-in. —
We’ve removed the thicker and more difficult to override border between table groups and moved it to an optional class you can apply,
.table-group-divider
.
See the table docs for an example.
Scrollspy has been rewritten
to use the Intersection Observer API
, which means you no longer need relative parent wrappers, deprecates
offset
config, and more. Look for your Scrollspy implementations to be more accurate and consistent in their nav highlighting.
Popovers and tooltips now use CSS variables.
Some CSS variables have been updated from their Sass counterparts to reduce the number of variables. As a result, three variables have been deprecated in this release:
$popover-arrow-color
,
$popover-arrow-outer-color
, and
$tooltip-arrow-color
.
Added new
.text-bg-{color}
helpers.
Instead of setting individual
.text-*
and
.bg-*
utilities, you can now use
the
.text-bg-*
helpers
to set a
background-color
with contrasting foreground
color
.
Added
.form-check-reverse
modifier to flip the order of labels and associated checkboxes/radios.
Added
striped columns
support to tables via the new
.table-striped-columns
class.
For a complete list of changes,
see the v5.2.0 project on GitHub
.
v5.1.0
Added experimental support for
CSS Grid layout
. —
This is a work in progress, and is not yet ready for production use, but you can opt into the new feature via Sass. To enable it, disable the default grid, by setting
$enable-grid-classes: false
and enable the CSS Grid by setting
$enable-cssgrid: true
.
Updated navbars to support offcanvas. —
Add
offcanvas drawers in any navbar
with the responsive
.navbar-expand-*
classes and some offcanvas markup.
Added new
placeholder component
. —
Our newest component, a way to provide temporary blocks in lieu of real content to help indicate that something is still loading in your site or app.
Collapse plugin now supports
horizontal collapsing
. —
Add
.collapse-horizontal
to your
.collapse
to collapse the
width
instead of the
height
. Avoid browser repainting by setting a
min-height
or
height
.
Added new stack and vertical rule helpers. —
Quickly apply multiple flexbox properties to quickly create custom layouts with
stacks
. Choose from horizontal (
.hstack
) and vertical (
.vstack
) stacks. Add vertical dividers similar to
<hr>
elements with the
new
.vr
helpers
.
Added new global
:root
CSS variables. —
Added several new CSS variables to the
:root
level for controlling
<body>
styles. More are in the works, including across our utilities and components, but for now read up
CSS variables in the Customize section
.
Overhauled color and background utilities to use CSS variables, and added new
text opacity
and
background opacity
utilities. —
.text-*
and
.bg-*
utilities are now built with CSS variables and
rgba()
color values, allowing you to easily customize any utility with new opacity utilities.
Added new snippet examples based to show how to customize our components. —
Pull ready to use customized components and other common design patterns with our new
Snippets examples
. Includes
footers
,
dropdowns
,
list groups
, and
modals
.
Removed unused positioning styles from popovers and tooltips
as these are handled solely by Popper.
$tooltip-margin
has been deprecated and set to
null
in the process.
Want more information?
Read the v5.1.0 blog post.
v5.0.0
Hey there!
Changes to our first major release of Bootstrap 5, v5.0.0, are documented below. They don’t reflect the additional changes shown above.
Dependencies
Dropped jQuery.
Upgraded from Popper v1.x to Popper v2.x.
Replaced Libsass with Dart Sass as our Sass compiler given Libsass was deprecated.
Migrated from Jekyll to Hugo for building our documentation
Browser support
Dropped Internet Explorer 10 and 11
Dropped Microsoft Edge < 16 (Legacy Edge)
Dropped Firefox < 60
Dropped Safari < 12
Dropped iOS Safari < 12
Dropped Chrome < 60
Documentation changes
Redesigned homepage, docs layout, and footer.
Added
new Parcel guide
.
Added
new Customize section
, replacing
v4’s Theming page
, with new details on Sass, global configuration options, color schemes, CSS variables, and more.
Reorganized all form documentation into
new Forms section
, breaking apart the content into more focused pages.
Similarly, updated
the Layout section
, to flesh out grid content more clearly.
Renamed “Navs” component page to "Navs & Tabs".
Renamed “Checks” page to "Checks & radios".
Redesigned the navbar and added a new subnav to make it easier to get around our sites and docs versions.
Added new keyboard shortcut for the search field:
Ctrl
+
/
.
Sass
We’ve ditched the default Sass map merges to make it easier to remove redundant values. Keep in mind you now have to define all values in the Sass maps like
$theme-colors
. Check out how to deal with
Sass maps
.
Breaking
Renamed
color-yiq()
function and related variables to
color-contrast()
as it’s no longer related to YIQ color space.
See #30168.
$yiq-contrasted-threshold
is renamed to
$min-contrast-ratio
.
$yiq-text-dark
and
$yiq-text-light
are respectively renamed to
$color-contrast-dark
and
$color-contrast-light
.
Breaking
Media query mixins parameters have changed for a more logical approach.
media-breakpoint-down()
uses the breakpoint itself instead of the next breakpoint (e.g.,
media-breakpoint-down(lg)
instead of
media-breakpoint-down(md)
targets viewports smaller than
lg
).
Similarly, the second parameter in
media-breakpoint-between()
also uses the breakpoint itself instead of the next breakpoint (e.g.,
media-breakpoint-between(sm, lg)
instead of
media-breakpoint-between(sm, md)
targets viewports between
sm
and
lg
).
Breaking
Removed print styles and
$enable-print-styles
variable. Print display classes are still around.
See #28339
.
Breaking
Dropped
color()
,
theme-color()
, and
gray()
functions in favor of variables.
See #29083
.
Breaking
Renamed
theme-color-level()
function to
color-level()
and now accepts any color you want instead of only
$theme-color
colors.
See #29083
Watch out:
color-level()
was later on dropped in
v5.0.0-alpha3
.
Breaking
Renamed
$enable-prefers-reduced-motion-media-query
and
$enable-pointer-cursor-for-buttons
to
$enable-reduced-motion
and
$enable-button-pointers
for brevity.
Breaking
Removed the
bg-gradient-variant()
mixin. Use the
.bg-gradient
class to add gradients to elements instead of the generated
.bg-gradient-*
classes.
Breaking
Removed previously deprecated mixins:
hover
,
hover-focus
,
plain-hover-focus
, and
hover-focus-active
float()
form-control-mixin()
nav-divider()
retina-img()
text-hide()
(also dropped the associated utility class,
.text-hide
)
visibility()
form-control-focus()
Breaking
Renamed
scale-color()
function to
shift-color()
to avoid collision with Sass’s own color scaling function.
box-shadow
mixins now allow
null
values and drop
none
from multiple arguments.
See #30394
.
The
border-radius()
mixin now has a default value.
Color system
The color system which worked with
color-level()
and
$theme-color-interval
was removed in favor of a new color system. All
lighten()
and
darken()
functions in our codebase are replaced by
tint-color()
and
shade-color()
. These functions will mix the color with either white or black instead of changing its lightness by a fixed amount. The
shift-color()
will either tint or shade a color depending on whether its weight parameter is positive or negative.
See #30622
for more details.
Added new tints and shades for every color, providing nine separate colors for each base color, as new Sass variables.
Improved color contrast. Bumped color contrast ratio from 3:1 to 4.5:1 and updated blue, green, cyan, and pink colors to ensure WCAG 2.2 AA contrast. Also changed our color contrast color from
$gray-900
to
$black
.
To support our color system, we’ve added new custom
tint-color()
and
shade-color()
functions to mix our colors appropriately.
Grid updates
New breakpoint!
Added new
xxl
breakpoint for
1400px
and up. No changes to all other breakpoints.
Improved gutters.
Gutters are now set in rems, and are narrower than v4 (
1.5rem
, or about
24px
, down from
30px
). This aligns our grid system’s gutters with our spacing utilities.
Added new
gutter class
(
.g-*
,
.gx-*
, and
.gy-*
) to control horizontal/vertical gutters, horizontal gutters, and vertical gutters.
Breaking
Renamed
.no-gutters
to
.g-0
to match new gutter utilities.
Columns no longer have
position: relative
applied, so you may have to add
.position-relative
to some elements to restore that behavior.
Breaking
Dropped several
.order-*
classes that often went unused. We now only provide
.order-0
to
.order-5
out of the box.
Breaking
Dropped the
.media
component as it can be easily replicated with utilities.
See #28265
and the
flex utilities page for an example
.
Breaking
bootstrap-grid.css
now only applies
box-sizing: border-box
to the column instead of resetting the global box-sizing. This way, our grid styles can be used in more places without interference.
$enable-grid-classes
no longer disables the generation of container classes anymore.
See #29146.
Updated the
make-col
mixin to default to equal columns without a specified size.
Content, Reboot, etc
RFS
is now enabled by default.
Headings using the
font-size()
mixin will automatically adjust their
font-size
to scale with the viewport.
This feature was previously opt-in with v4.
Breaking
Overhauled our display typography to replace our
$display-*
variables and with a
$display-font-sizes
Sass map. Also removed the individual
$display-*-weight
variables for a single
$display-font-weight
and adjusted
font-size
s.
Added two new
.display-*
heading sizes,
.display-5
and
.display-6
.
Links are underlined by default
(not just on hover), unless they’re part of specific components.
Redesigned tables
to refresh their styles and rebuild them with CSS variables for more control over styling.
Breaking
Nested tables do not inherit styles anymore.
Breaking
.thead-light
and
.thead-dark
are dropped in favor of the
.table-*
variant classes which can be used for all table elements (
thead
,
tbody
,
tfoot
,
tr
,
th
and
td
).
Breaking
The
table-row-variant()
mixin is renamed to
table-variant()
and accepts only 2 parameters:
$color
(color name) and
$value
(color code). The border color and accent colors are automatically calculated based on the table factor variables.
Split table cell padding variables into
-y
and
-x
.
Breaking
Dropped
.pre-scrollable
class.
See #29135
Breaking
.text-*
utilities do not add hover and focus states to links anymore.
.link-*
helper classes can be used instead.
See #29267
Breaking
Dropped
.text-justify
class.
See #29793
Breaking
<hr>
elements now use
height
instead of
border
to better support the
size
attribute. This also enables use of padding utilities to create thicker dividers (e.g.,
<hr class="py-1">
).
Reset default horizontal
padding-left
on
<ul>
and
<ol>
elements from browser default
40px
to
2rem
.
Added
$enable-smooth-scroll
, which applies
scroll-behavior: smooth
globally—except for users asking for reduced motion through
prefers-reduced-motion
media query.
See #31877
RTL
Horizontal direction specific variables, utilities, and mixins have all been renamed to use logical properties like those found in flexbox layouts—e.g.,
start
and
end
in lieu of
left
and
right
.
Forms
Added new floating forms!
We’ve promoted the Floating labels example to fully supported form components.
See the new Floating labels page.
Breaking
Consolidated native and custom form elements.
Checkboxes, radios, selects, and other inputs that had native and custom classes in v4 have been consolidated. Now nearly all our form elements are entirely custom, most without the need for custom HTML.
.custom-control.custom-checkbox
is now
.form-check
.
.custom-control.custom-radio
is now
.form-check
.
.custom-control.custom-switch
is now
.form-check.form-switch
.
.custom-select
is now
.form-select
.
.custom-file
and
.form-control-file
have been replaced by custom styles on top of
.form-control
.
.custom-range
is now
.form-range
.
Dropped native
.form-control-file
and
.form-control-range
.
Breaking
Dropped
.input-group-append
and
.input-group-prepend
. You can now just add buttons and
.input-group-text
as direct children of the input groups.
The longstanding
Missing border radius on input group with validation feedback bug
is finally fixed by adding an additional
.has-validation
class to input groups with validation.
Breaking
Dropped form-specific layout classes for our grid system.
Use our grid and utilities instead of
.form-group
,
.form-row
, or
.form-inline
.
Breaking
Form labels now require
.form-label
.
Breaking
.form-text
no longer sets
display
, allowing you to create inline or block help text as you wish just by changing the HTML element.
Form controls no longer used fixed
height
when possible, instead deferring to
min-height
to improve customization and compatibility with other components.
Validation icons are no longer applied to
<select>
s with
multiple
.
Rearranged source Sass files under
scss/forms/
, including input group styles.
Components
Unified
padding
values for alerts, breadcrumbs, cards, dropdowns, list groups, modals, popovers, and tooltips to be based on our
$spacer
variable.
See #30564
.
Accordion
Added
new accordion component
.
Alerts
Alerts now have
examples with icons
.
Removed custom styles for
<hr>
s in each alert since they already use
currentColor
.
Badges
Breaking
Dropped all
.badge-*
color classes for background utilities (e.g., use
.bg-primary
instead of
.badge-primary
).
Breaking
Dropped
.badge-pill
—use the
.rounded-pill
utility instead.
Breaking
Removed hover and focus styles for
<a>
and
<button>
elements.
Increased default padding for badges from
.25em
/
.5em
to
.35em
/
.65em
.
Breadcrumbs
Simplified the default appearance of breadcrumbs by removing
padding
,
background-color
, and
border-radius
.
Added new CSS custom property
--bs-breadcrumb-divider
for easy customization without needing to recompile CSS.
Buttons
Breaking
Toggle buttons
, with checkboxes or radios, no longer require JavaScript and have new markup.
We no longer require a wrapping element, add
.btn-check
to the
<input>
, and pair it with any
.btn
classes on the
<label>
.
See #30650
.
The docs for this has moved from our Buttons page to the new Forms section.
Breaking
Dropped
.btn-block
for utilities.
Instead of using
.btn-block
on the
.btn
, wrap your buttons with
.d-grid
and a
.gap-*
utility to space them as needed. Switch to responsive classes for even more control over them.
Read the docs for some examples.
Updated our
button-variant()
and
button-outline-variant()
mixins to support additional parameters.
Updated buttons to ensure increased contrast on hover and active states.
Disabled buttons now have
pointer-events: none;
.
Card
Breaking
Dropped
.card-deck
in favor of our grid. Wrap your cards in column classes and add a parent
.row-cols-*
container to recreate card decks (but with more control over responsive alignment).
Breaking
Dropped
.card-columns
in favor of Masonry.
See #28922
.
Breaking
Replaced the
.card
based accordion with a
new Accordion component
.
Carousel
Added new
.carousel-dark
variant
for dark text, controls, and indicators (great for lighter backgrounds).
Replaced chevron icons for carousel controls with new SVGs from
Bootstrap Icons
.
Close button
Breaking
Renamed
.close
to
.btn-close
for a less generic name.
Close buttons now use a
background-image
(embedded SVG) instead of a
&times;
in the HTML, allowing for easier customization without the need to touch your markup.
Added new
.btn-close-white
variant that uses
filter: invert(1)
to enable higher contrast dismiss icons against darker backgrounds.
Collapse
Removed scroll anchoring for accordions.
Dropdowns
Added new
.dropdown-menu-dark
variant and associated variables for on-demand dark dropdowns.
Added new variable for
$dropdown-padding-x
.
Darkened the dropdown divider for improved contrast.
Breaking
All the events for the dropdown are now triggered on the dropdown toggle button and then bubbled up to the parent element.
Dropdown menus now have a
data-bs-popper="static"
attribute set when the positioning of the dropdown is static, or dropdown is in the navbar. This is added by our JavaScript and helps us use custom position styles without interfering with Popper’s positioning.
Breaking
Dropped
flip
option for dropdown plugin in favor of native Popper configuration. You can now disable the flipping behavior by passing an empty array for
fallbackPlacements
option in
flip
modifier.
Dropdown menus can now be clickable with a new
autoClose
option to handle the
auto close behavior
. You can use this option to accept the click inside or outside the dropdown menu to make it interactive.
Dropdowns now support
.dropdown-item
s wrapped in
<li>
s.
Jumbotron
Breaking
Dropped the jumbotron component as it can be replicated with utilities.
See our new Jumbotron example for a demo.
List group
Added new
.list-group-numbered
modifier
to list groups.
Navs and tabs
Added new
null
variables for
font-size
,
font-weight
,
color
, and
:hover
color
to the
.nav-link
class.
Navbars
Breaking
Navbars now require a container within (to drastically simplify spacing requirements and CSS required).
Breaking
The
.active
class can no longer be applied to
.nav-item
s, it must be applied directly on
.nav-link
s.
Offcanvas
Added the new
offcanvas component
.
Pagination
Pagination links now have customizable
margin-left
that are dynamically rounded on all corners when separated from one another.
Added
transition
s to pagination links.
Popovers
Breaking
Renamed
.arrow
to
.popover-arrow
in our default popover template.
Renamed
whiteList
option to
allowList
.
Spinners
Spinners now honor
prefers-reduced-motion: reduce
by slowing down animations.
See #31882
.
Improved spinner vertical alignment.
Toasts
Toasts can now be
positioned
in a
.toast-container
with the help of
positioning utilities
.
Changed default toast duration to 5 seconds.
Removed
overflow: hidden
from toasts and replaced with proper
border-radius
s with
calc()
functions.
Tooltips
Breaking
Renamed
.arrow
to
.tooltip-arrow
in our default tooltip template.
Breaking
The default value for the
fallbackPlacements
is changed to
['top', 'right', 'bottom', 'left']
for better placement of popper elements.
Breaking
Renamed
whiteList
option to
allowList
.
Utilities
Breaking
Renamed several utilities to use logical property names instead of directional names with the addition of RTL support:
Renamed
.float-left
and
.float-right
to
.float-start
and
.float-end
.
Renamed
.border-left
and
.border-right
to
.border-start
and
.border-end
.
Renamed
.rounded-left
and
.rounded-right
to
.rounded-start
and
.rounded-end
.
Renamed
.ml-*
and
.mr-*
to
.ms-*
and
.me-*
.
Renamed
.pl-*
and
.pr-*
to
.ps-*
and
.pe-*
.
Renamed
.text-*-left
and
.text-*-right
to
.text-*-start
and
.text-*-end
.
Breaking
Disabled negative margins by default.
Added new
.bg-body
class for quickly setting the
<body>
’s background to additional elements.
Added new
position utilities
for
top
,
right
,
bottom
, and
left
. Values include
0
,
50%
, and
100%
for each property.
Added new
.translate-middle-x
&
.translate-middle-y
utilities to horizontally or vertically center absolute/fixed positioned elements.
Added new
border-width
utilities
.
Breaking
Renamed
.text-monospace
to
.font-monospace
.
Breaking
Removed
.text-hide
as it’s an antiquated method for hiding text that shouldn’t be used anymore.
Added
.fs-*
utilities for
font-size
utilities (with RFS enabled). These use the same scale as HTML’s default headings (1-6, large to small), and can be modified via Sass map.
Breaking
Renamed
.font-weight-*
utilities as
.fw-*
for brevity and consistency.
Breaking
Renamed
.font-italic
utility to
.fst-italic
for brevity and consistency with new
.fst-normal
utility.
Added
.d-grid
to display utilities and new
gap
utilities (
.gap
) for CSS Grid and flexbox layouts.
Breaking
Removed
.rounded-sm
and
rounded-lg
, and introduced a new scale of classes,
.rounded-0
to
.rounded-3
.
See #31687
.
Added new
line-height
utilities:
.lh-1
,
.lh-sm
,
.lh-base
and
.lh-lg
. See
here
.
Moved the
.d-none
utility in our CSS to give it more weight over other display utilities.
Extended the
.visually-hidden-focusable
helper to also work on containers, using
:focus-within
.
Helpers
Breaking
Responsive embed helpers have been renamed to
ratio helpers
with new class names and improved behaviors, as well as a helpful CSS variable.
Classes have been renamed to change
by
to
x
in the aspect ratio. For example,
.ratio-16by9
is now
.ratio-16x9
.
We’ve dropped the
.embed-responsive-item
and element group selector in favor of a simpler
.ratio > *
selector. No more class is needed, and the ratio helper now works with any HTML element.
The
$embed-responsive-aspect-ratios
Sass map has been renamed to
$aspect-ratios
and its values have been simplified to include the class name and the percentage as the
key: value
pair.
CSS variables are now generated and included for each value in the Sass map. Modify the
--bs-aspect-ratio
variable on the
.ratio
to create any
custom aspect ratio
.
Breaking
"Screen reader" classes are now
"visually hidden" classes
.
Changed the Sass file from
scss/helpers/_screenreaders.scss
to
scss/helpers/_visually-hidden.scss
Renamed
.sr-only
and
.sr-only-focusable
to
.visually-hidden
and
.visually-hidden-focusable
Renamed
sr-only()
and
sr-only-focusable()
mixins to
visually-hidden()
and
visually-hidden-focusable()
.
bootstrap-utilities.css
now also includes our helpers. Helpers don’t need to be imported in custom builds anymore.
JavaScript
Dropped jQuery dependency
and rewrote plugins to be in regular JavaScript.
Breaking
Data attributes for all JavaScript plugins are now namespaced to help distinguish Bootstrap functionality from third parties and your own code. For example, we use
data-bs-toggle
instead of
data-toggle
.
All plugins can now accept a CSS selector as the first argument.
You can either pass a DOM element or any valid CSS selector to create a new instance of the plugin:
const
modal
=
new
bootstrap
.
Modal
(
'#myModal'
)
const
dropdown
=
new
bootstrap
.
Dropdown
(
'[data-bs-toggle="dropdown"]'
)
popperConfig
can be passed as a function that accepts the Bootstrap’s default Popper config as an argument, so that you can merge this default configuration in your way.
Applies to dropdowns, popovers, and tooltips.
The default value for the
fallbackPlacements
is changed to
['top', 'right', 'bottom', 'left']
for better placement of Popper elements.
Applies to dropdowns, popovers, and tooltips.
Removed underscore from public static methods like
_getInstance()
→
getInstance()
.
Removed
util.js
, with its functionality now integrated into individual plugins. If you previously included
util.js
manually, you can safely remove it, as it is no longer needed. Each plugin now contains only the utilities it requires, enhancing modularity and reducing dependencies.


## Contents · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/getting-started/contents/
- fetched_at: 2026-04-29T13:45:46.222538+00:00

View on GitHub
Contents
Discover what’s included in Bootstrap, including our compiled and source code flavors.
On this page
Compiled Bootstrap
Once downloaded, unzip the compressed folder and you’ll see something like this:
bootstrap/
├── css/
│ ├── bootstrap-grid.css
│ ├── bootstrap-grid.css.map
│ ├── bootstrap-grid.min.css
│ ├── bootstrap-grid.min.css.map
│ ├── bootstrap-grid.rtl.css
│ ├── bootstrap-grid.rtl.css.map
│ ├── bootstrap-grid.rtl.min.css
│ ├── bootstrap-grid.rtl.min.css.map
│ ├── bootstrap-reboot.css
│ ├── bootstrap-reboot.css.map
│ ├── bootstrap-reboot.min.css
│ ├── bootstrap-reboot.min.css.map
│ ├── bootstrap-reboot.rtl.css
│ ├── bootstrap-reboot.rtl.css.map
│ ├── bootstrap-reboot.rtl.min.css
│ ├── bootstrap-reboot.rtl.min.css.map
│ ├── bootstrap-utilities.css
│ ├── bootstrap-utilities.css.map
│ ├── bootstrap-utilities.min.css
│ ├── bootstrap-utilities.min.css.map
│ ├── bootstrap-utilities.rtl.css
│ ├── bootstrap-utilities.rtl.css.map
│ ├── bootstrap-utilities.rtl.min.css
│ ├── bootstrap-utilities.rtl.min.css.map
│ ├── bootstrap.css
│ ├── bootstrap.css.map
│ ├── bootstrap.min.css
│ ├── bootstrap.min.css.map
│ ├── bootstrap.rtl.css
│ ├── bootstrap.rtl.css.map
│ ├── bootstrap.rtl.min.css
│ └── bootstrap.rtl.min.css.map
└── js/
 ├── bootstrap.bundle.js
 ├── bootstrap.bundle.js.map
 ├── bootstrap.bundle.min.js
 ├── bootstrap.bundle.min.js.map
 ├── bootstrap.esm.js
 ├── bootstrap.esm.js.map
 ├── bootstrap.esm.min.js
 ├── bootstrap.esm.min.js.map
 ├── bootstrap.js
 ├── bootstrap.js.map
 ├── bootstrap.min.js
 └── bootstrap.min.js.map
This is the most basic form of Bootstrap: compiled files for quick drop-in usage in nearly any web project. We provide compiled CSS and JS (
bootstrap.*
), as well as compiled and minified CSS and JS (
bootstrap.min.*
).
Source maps
(
bootstrap.*.map
) are available for use with certain browsers’ developer tools. Bundled JS files (
bootstrap.bundle.js
and minified
bootstrap.bundle.min.js
) include
Popper
.
CSS files
Bootstrap includes a handful of options for including some or all of our compiled CSS.
CSS files
Layout
Content
Components
Utilities
bootstrap.css
bootstrap.min.css
bootstrap.rtl.css
bootstrap.rtl.min.css
Included
Included
Included
Included
bootstrap-grid.css
bootstrap-grid.rtl.css
bootstrap-grid.min.css
bootstrap-grid.rtl.min.css
Only grid system
—
—
Only flex utilities
bootstrap-utilities.css
bootstrap-utilities.rtl.css
bootstrap-utilities.min.css
bootstrap-utilities.rtl.min.css
—
—
—
Included
bootstrap-reboot.css
bootstrap-reboot.rtl.css
bootstrap-reboot.min.css
bootstrap-reboot.rtl.min.css
—
Only Reboot
—
—
JS files
Similarly, we have options for including some or all of our compiled JavaScript.
JS Files
Popper
bootstrap.bundle.js
bootstrap.bundle.min.js
Included
bootstrap.js
bootstrap.min.js
–
Bootstrap source code
The Bootstrap source code download includes the compiled CSS and JavaScript assets, along with source Sass, JavaScript, and documentation. More specifically, it includes the following and more:
bootstrap/
├── dist/
│ ├── css/
│ └── js/
├── site/
│ └──content/
│ └── docs/
│ └── 5.3/
│ └── examples/
├── js/
└── scss/
The
scss/
and
js/
are the source code for our CSS and JavaScript. The
dist/
folder includes everything listed in the compiled download section above. The
site/content/docs/
folder includes the source code for our hosted documentation, including our live examples of Bootstrap usage.
Beyond that, any other included file provides support for packages, license information, and development.


## Headers · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/examples/headers/
- fetched_at: 2026-04-29T13:45:46.687582+00:00

Headers examples
Simple header
Home
Features
Pricing
FAQs
About
Home
Features
Pricing
FAQs
About
Home
Features
Pricing
FAQs
About
Home
Features
Pricing
FAQs
About
Overview
Inventory
Customers
Products
New project...
Settings
Profile
Sign out
Overview
Inventory
Customers
Products
Reports
Analytics
New project...
Settings
Profile
Sign out
Double header
Home
Dashboard
Orders
Products
Customers


## Heroes · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/examples/heroes/
- fetched_at: 2026-04-29T13:45:46.982092+00:00

Heroes examples
Centered hero
Quickly design and customize responsive mobile-first sites with Bootstrap, the world’s most popular front-end open source toolkit, featuring Sass variables and mixins, responsive grid system, extensive prebuilt components, and powerful JavaScript plugins.
Centered screenshot
Quickly design and customize responsive mobile-first sites with Bootstrap, the world’s most popular front-end open source toolkit, featuring Sass variables and mixins, responsive grid system, extensive prebuilt components, and powerful JavaScript plugins.
Responsive left-aligned hero with image
Quickly design and customize responsive mobile-first sites with Bootstrap, the world’s most popular front-end open source toolkit, featuring Sass variables and mixins, responsive grid system, extensive prebuilt components, and powerful JavaScript plugins.
Vertically centered hero sign-up form
Below is an example form built entirely with Bootstrap’s form controls. Each required form group has a validation state that can be triggered by attempting to submit the form without completing it.
Border hero with cropped image and shadows
Quickly design and customize responsive mobile-first sites with Bootstrap, the world’s most popular front-end open source toolkit, featuring Sass variables and mixins, responsive grid system, extensive prebuilt components, and powerful JavaScript plugins.
Dark color hero
Quickly design and customize responsive mobile-first sites with Bootstrap, the world’s most popular front-end open source toolkit, featuring Sass variables and mixins, responsive grid system, extensive prebuilt components, and powerful JavaScript plugins.


## Features · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/examples/features/
- fetched_at: 2026-04-29T13:45:47.292604+00:00

Features examples
Columns with icons
Featured title
Paragraph of text beneath the heading to explain the heading. We'll add onto it with another sentence and probably just keep going until we run out of words.
Call to action
Featured title
Paragraph of text beneath the heading to explain the heading. We'll add onto it with another sentence and probably just keep going until we run out of words.
Call to action
Featured title
Paragraph of text beneath the heading to explain the heading. We'll add onto it with another sentence and probably just keep going until we run out of words.
Call to action
Hanging icons
Featured title
Paragraph of text beneath the heading to explain the heading. We'll add onto it with another sentence and probably just keep going until we run out of words.
Primary button
Featured title
Paragraph of text beneath the heading to explain the heading. We'll add onto it with another sentence and probably just keep going until we run out of words.
Primary button
Featured title
Paragraph of text beneath the heading to explain the heading. We'll add onto it with another sentence and probably just keep going until we run out of words.
Primary button
Custom cards
Short title, long jacket
Earth
3d
Much longer title that wraps to multiple lines
Pakistan
4d
Another longer title belongs here
California
5d
Icon grid
Featured title
Paragraph of text beneath the heading to explain the heading.
Featured title
Paragraph of text beneath the heading to explain the heading.
Featured title
Paragraph of text beneath the heading to explain the heading.
Featured title
Paragraph of text beneath the heading to explain the heading.
Featured title
Paragraph of text beneath the heading to explain the heading.
Featured title
Paragraph of text beneath the heading to explain the heading.
Featured title
Paragraph of text beneath the heading to explain the heading.
Featured title
Paragraph of text beneath the heading to explain the heading.
Features with title
Left-aligned title explaining these awesome features
Paragraph of text beneath the heading to explain the heading. We'll add onto it with another sentence and probably just keep going until we run out of words.
Primary button
Featured title
Paragraph of text beneath the heading to explain the heading.
Featured title
Paragraph of text beneath the heading to explain the heading.
Featured title
Paragraph of text beneath the heading to explain the heading.
Featured title
Paragraph of text beneath the heading to explain the heading.


## Sidebars · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/examples/sidebars/
- fetched_at: 2026-04-29T13:45:47.628116+00:00

Sidebars examples
Sidebar
Home
Dashboard
Orders
Products
Customers
mdo
New project...
Settings
Profile
Sign out
Sidebar
Home
Dashboard
Orders
Products
Customers
mdo
New project...
Settings
Profile
Sign out
Icon-only
New project...
Settings
Profile
Sign out
Collapsible
Overview
Updates
Reports
Overview
Weekly
Monthly
Annually
New
Processed
Shipped
Returned
New...
Profile
Settings
Sign out
List group
List group item heading
Wed
Some placeholder content in a paragraph below the heading and date.
List group item heading
Tues
Some placeholder content in a paragraph below the heading and date.
List group item heading
Mon
Some placeholder content in a paragraph below the heading and date.
List group item heading
Wed
Some placeholder content in a paragraph below the heading and date.
List group item heading
Tues
Some placeholder content in a paragraph below the heading and date.
List group item heading
Mon
Some placeholder content in a paragraph below the heading and date.
List group item heading
Wed
Some placeholder content in a paragraph below the heading and date.
List group item heading
Tues
Some placeholder content in a paragraph below the heading and date.
List group item heading
Mon
Some placeholder content in a paragraph below the heading and date.
List group item heading
Wed
Some placeholder content in a paragraph below the heading and date.
List group item heading
Tues
Some placeholder content in a paragraph below the heading and date.
List group item heading
Mon
Some placeholder content in a paragraph below the heading and date.


## Dropdowns · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/examples/dropdowns/
- fetched_at: 2026-04-29T13:45:48.171787+00:00

Action
Another action
Something else here
Separated link
Action
Another action
Something else here
Separated link
Action
Another action
Something else here
Separated link
Action
Another action
Something else here
Separated link
Documents
Photos
Movies
Music
Games
Trash
Documents
Photos
Movies
Music
Games
Trash
June
January
February
March
April
May
June
July
August
September
October
November
December
Sun
Mon
Tue
Wed
Thu
Fri
Sat
June
January
February
March
April
May
June
July
August
September
October
November
December
Sun
Mon
Tue
Wed
Thu
Fri
Sat


## List groups · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/examples/list-groups/
- fetched_at: 2026-04-29T13:45:48.511313+00:00

List group item heading
Some placeholder content in a paragraph.
now
Another title here
Some placeholder content in a paragraph that goes a little longer so it wraps to a new line.
3d
Third heading
Some placeholder content in a paragraph.
1w
First checkbox
With support text underneath to add more detail
Second checkbox
Some other text goes here
Third checkbox
And we end with another snippet of text
First radio
With support text underneath to add more detail
Second radio
Some other text goes here
Third radio
And we end with another snippet of text
Finish sales report
1:00–2:00pm
Weekly All Hands
2:00–2:30pm
Out of office
Tomorrow
Add new task...
Choose list...
First radio
With support text underneath to add more detail
Second radio
Some other text goes here
Third radio
And we end with another snippet of text
Fourth disabled radio
This option is disabled
First radio
With support text underneath to add more detail
Second radio
Some other text goes here
Third radio
And we end with another snippet of text
Fourth disabled radio
This option is disabled


## Modals · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/examples/modals/
- fetched_at: 2026-04-29T13:45:48.817833+00:00

Modal title
This is a modal sheet, a variation of the modal that docs itself to the bottom of the viewport like the newer share sheets in iOS.
Enable this setting?
You can always change your mind in your account settings.
What's new
Grid view
Not into lists? Try the new grid view.
Bookmarks
Save items you love for easy access later.
Video embeds
Share videos wherever you go.
Sign up for free


## Badges · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/examples/badges/
- fetched_at: 2026-04-29T13:45:49.139344+00:00

Primary
Secondary
Success
Danger
Warning
Info
Light
Dark
Primary
Secondary
Success
Danger
Warning
Info
Light
Dark
Primary
Secondary
Success
Danger
Warning
Info
Light
Dark
Primary
Secondary
Success
Danger
Warning
Info
Light
Dark
Primary 1
Primary 2
Primary 3
Primary
Secondary
Success
Danger
Warning
Info
Light
Dark


## Jumbotrons · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/examples/jumbotrons/
- fetched_at: 2026-04-29T13:45:50.100448+00:00

Jumbotron with icon
This is a custom jumbotron featuring an SVG image at the top, some longer text that wraps early thanks to a responsive
.col-*
class, and a customized call to action.
Placeholder jumbotron
This faded back jumbotron is useful for placeholder content. It's also a great way to add a bit of context to a page or section when no content is available and to encourage visitors to take a specific action.
Full-width jumbotron
This takes the basic jumbotron above and makes its background edge-to-edge with a
.container
inside to align content. Similar to above, it's been recreated with built-in grid and utility classes.
Basic jumbotron
This is a simple Bootstrap jumbotron that sits within a
.container
, recreated with built-in utility classes.


## Album example · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/examples/album/
- fetched_at: 2026-04-29T13:45:50.408094+00:00

Album example
Something short and leading about the collection below—its contents, the creator, etc. Make it short and sweet, but not too short so folks don’t simply skip over it entirely.
Main call to action
Secondary action
This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.
9 mins
This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.
9 mins
This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.
9 mins
This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.
9 mins
This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.
9 mins
This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.
9 mins
This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.
9 mins
This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.
9 mins
This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.
9 mins


## Pricing example · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/examples/pricing/
- fetched_at: 2026-04-29T13:45:50.784606+00:00

Free
$0
/mo
10 users included
2 GB of storage
Email support
Help center access
Pro
$15
/mo
20 users included
10 GB of storage
Priority email support
Help center access
Enterprise
$29
/mo
30 users included
15 GB of storage
Phone and email support
Help center access
Compare plans
Free
Pro
Enterprise
Public
Private
Permissions
Sharing
Unlimited members
Extra security


## Checkout example · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/examples/checkout/
- fetched_at: 2026-04-29T13:45:51.117123+00:00

Checkout form
Below is an example form built entirely with Bootstrap’s form controls. Each required form group has a validation state that can be triggered by attempting to submit the form without completing it.
Your cart
3
Product name
Brief description
$12
Second product
Brief description
$8
Third item
Brief description
$5
Promo code
EXAMPLECODE
−$5
Total (USD)
$20
Billing address


## Product example · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/examples/product/
- fetched_at: 2026-04-29T13:45:51.423635+00:00

Designed for engineers
Build anything you want with Aperture
Learn more
Buy
Another headline
And an even wittier subheading.
Another headline
And an even wittier subheading.
Another headline
And an even wittier subheading.
Another headline
And an even wittier subheading.
Another headline
And an even wittier subheading.
Another headline
And an even wittier subheading.
Another headline
And an even wittier subheading.
Another headline
And an even wittier subheading.


## Carousel Template · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/examples/carousel/
- fetched_at: 2026-04-29T13:45:52.150655+00:00

Example headline.
Some representative placeholder content for the first slide of the carousel.
Sign up today
Another example headline.
Some representative placeholder content for the second slide of the carousel.
Learn more
One more for good measure.
Some representative placeholder content for the third slide of this carousel.
Browse gallery
Heading
Some representative placeholder content for the three columns of text below the carousel. This is the first column.
View details »
Heading
Another exciting bit of representative placeholder content. This time, we've moved on to the second column.
View details »
Heading
And lastly this, the third column of representative placeholder content.
View details »
First featurette heading.
It’ll blow your mind.
Some great placeholder content for the first featurette here. Imagine some exciting prose here.
Oh yeah, it’s that good.
See for yourself.
Another featurette? Of course. More placeholder content here to give you an idea of how this layout would work with some actual real-world content in place.
And lastly, this one.
Checkmate.
And yes, this is the last block of representative placeholder content. Again, not really intended to be actually read, simply here to give you a better view of what this would look like with some actual content. Your content.


## Blog Template · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/examples/blog/
- fetched_at: 2026-04-29T13:45:52.467516+00:00

Title of a longer featured blog post
Multiple lines of text that form the lede, informing new readers quickly and efficiently about what’s most interesting in this post’s contents.
Continue reading...
World
Featured post
Nov 12
This is a wider card with supporting text below as a natural lead-in to additional content.
Continue reading
Design
Post title
Nov 11
This is a wider card with supporting text below as a natural lead-in to additional content.
Continue reading
From the Firehose
Sample blog post
January 1, 2021 by
Mark
This blog post shows a few different types of content that’s supported and styled with Bootstrap. Basic typography, lists, tables, images, code, and more are all supported as expected.
This is some additional paragraph placeholder content. It has been written to fill the available space and show how a longer snippet of text affects the surrounding content. We'll repeat it often to keep the demonstration flowing, so be on the lookout for this exact same string of text.
Blockquotes
This is an example blockquote in action:
Quoted text goes here.
This is some additional paragraph placeholder content. It has been written to fill the available space and show how a longer snippet of text affects the surrounding content. We'll repeat it often to keep the demonstration flowing, so be on the lookout for this exact same string of text.
Example lists
This is some additional paragraph placeholder content. It's a slightly shorter version of the other highly repetitive body text used throughout. This is an example unordered list:
First list item
Second list item with a longer description
Third list item to close it out
And this is an ordered list:
First list item
Second list item with a longer description
Third list item to close it out
And this is a definition list:
HyperText Markup Language (HTML)
The language used to describe and define the content of a Web page
Cascading Style Sheets (CSS)
Used to describe the appearance of Web content
JavaScript (JS)
The programming language used to build advanced Web sites and applications
Inline HTML elements
HTML defines a long list of available inline tags, a complete list of which can be found on the
Mozilla Developer Network
.
To bold text
, use
<strong>
.
To italicize text
, use
<em>
.
Abbreviations, like
HTML
should use
<abbr>
, with an optional
title
attribute for the full phrase.
Citations, like
— Mark Otto
, should use
<cite>
.
Deleted
text should use
<del>
and
inserted
text should use
<ins>
.
Superscript
text
uses
<sup>
and subscript
text
uses
<sub>
.
Most of these elements are styled by browsers with few modifications on our part.
Heading
This is some additional paragraph placeholder content. It has been written to fill the available space and show how a longer snippet of text affects the surrounding content. We'll repeat it often to keep the demonstration flowing, so be on the lookout for this exact same string of text.
Sub-heading
This is some additional paragraph placeholder content. It has been written to fill the available space and show how a longer snippet of text affects the surrounding content. We'll repeat it often to keep the demonstration flowing, so be on the lookout for this exact same string of text.
Example code block
This is some additional paragraph placeholder content. It's a slightly shorter version of the other highly repetitive body text used throughout.
Another blog post
December 23, 2020 by
Jacob
This is some additional paragraph placeholder content. It has been written to fill the available space and show how a longer snippet of text affects the surrounding content. We'll repeat it often to keep the demonstration flowing, so be on the lookout for this exact same string of text.
Longer quote goes here, maybe with some
emphasized text
in the middle of it.
This is some additional paragraph placeholder content. It has been written to fill the available space and show how a longer snippet of text affects the surrounding content. We'll repeat it often to keep the demonstration flowing, so be on the lookout for this exact same string of text.
Example table
And don't forget about tables in these posts:
Name
Upvotes
Downvotes
Alice
10
11
Bob
4
3
Charlie
7
9
Totals
21
23
This is some additional paragraph placeholder content. It's a slightly shorter version of the other highly repetitive body text used throughout.
New feature
December 14, 2020 by
Chris
This is some additional paragraph placeholder content. It has been written to fill the available space and show how a longer snippet of text affects the surrounding content. We'll repeat it often to keep the demonstration flowing, so be on the lookout for this exact same string of text.
First list item
Second list item with a longer description
Third list item to close it out
This is some additional paragraph placeholder content. It's a slightly shorter version of the other highly repetitive body text used throughout.
About
Customize this section to tell your visitors a little bit about your publication, writers, content, or something else entirely. Totally up to you.
Recent posts
Example blog post title
January 15, 2024
This is another blog post title
January 14, 2024
Longer blog post title: This one has multiple lines!
January 13, 2024
Archives
March 2021
February 2021
January 2021
December 2020
November 2020
October 2020
September 2020
August 2020
July 2020
June 2020
May 2020
April 2020
Elsewhere
GitHub
Social
Facebook


## Dashboard Template · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/examples/dashboard/
- fetched_at: 2026-04-29T13:45:52.821032+00:00

Dashboard
Section title
#
Header
Header
Header
Header
1,001
random
data
placeholder
text
1,002
placeholder
irrelevant
visual
layout
1,003
data
rich
dashboard
tabular
1,003
information
placeholder
illustrative
data
1,004
text
random
layout
dashboard
1,005
dashboard
irrelevant
text
placeholder
1,006
dashboard
illustrative
rich
data
1,007
placeholder
tabular
information
irrelevant
1,008
random
data
placeholder
text
1,009
placeholder
irrelevant
visual
layout
1,010
data
rich
dashboard
tabular
1,011
information
placeholder
illustrative
data
1,012
text
placeholder
layout
dashboard
1,013
dashboard
irrelevant
text
visual
1,014
dashboard
illustrative
rich
data
1,015
random
tabular
information
text


## Sticky Footer Navbar Template · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/examples/sticky-footer-navbar/
- fetched_at: 2026-04-29T13:45:53.756581+00:00

Sticky footer with fixed navbar
Pin a footer to the bottom of the viewport in desktop browsers with this custom HTML and CSS. A fixed navbar has been added with
padding-top: 60px;
on the
main > .container
.
Back to
the default sticky footer
minus the navbar.


## Jumbotron example · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/examples/jumbotron/
- fetched_at: 2026-04-29T13:45:54.071091+00:00

Jumbotron example
Custom jumbotron
Using a series of utilities, you can create this jumbotron, just like the one in previous versions of Bootstrap. Check out the examples below for how you can remix and restyle it to your liking.
Change the background
Swap the background-color utility and add a `.text-*` color utility to mix up the jumbotron look. Then, mix and match with additional component themes and more.
Add borders
Or, keep it light and add a border for some added definition to the boundaries of your content. Be sure to look under the hood at the source HTML here as we've adjusted the alignment and sizing of both column's content for equal-height.


## Starter Template · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/examples/starter-template/
- fetched_at: 2026-04-29T13:45:54.373093+00:00

Get started with Bootstrap
Quickly and easily get started with Bootstrap's compiled, production-ready files with this barebones example featuring some basic HTML and helpful links. Download all our examples to get started.
Download examples
Starter projects
Ready to go beyond the starter template? Check out these open source projects that you can quickly duplicate to a new GitHub repository.
Bootstrap npm starter
Bootstrap Parcel starter
Bootstrap Vite starter
Bootstrap Webpack starter
Guides
Read more detailed instructions and documentation on using or contributing to Bootstrap.
Bootstrap quick start guide
Bootstrap Webpack guide
Bootstrap Parcel guide
Bootstrap Vite guide
Contributing to Bootstrap


## Grid Template · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/examples/grid/
- fetched_at: 2026-04-29T13:45:54.706331+00:00

Bootstrap grid examples
Basic grid layouts to get you familiar with building within the Bootstrap grid system.
In these examples the
.themed-grid-col
class is added to the columns to add some theming. This is not a class that is available in Bootstrap by default.
Five grid tiers
There are five tiers to the Bootstrap grid system, one for each range of devices we support. Each tier starts at a minimum viewport size and automatically applies to the larger devices unless overridden.
.col-4
.col-4
.col-4
.col-sm-4
.col-sm-4
.col-sm-4
.col-md-4
.col-md-4
.col-md-4
.col-lg-4
.col-lg-4
.col-lg-4
.col-xl-4
.col-xl-4
.col-xl-4
.col-xxl-4
.col-xxl-4
.col-xxl-4
Three equal columns
Get three equal-width columns
starting at desktops and scaling to large desktops
. On mobile devices, tablets and below, the columns will automatically stack.
.col-md-4
.col-md-4
.col-md-4
Three equal columns alternative
By using the
.row-cols-*
classes, you can easily create a grid with equal columns.
.col
child of
.row-cols-md-3
.col
child of
.row-cols-md-3
.col
child of
.row-cols-md-3
Three unequal columns
Get three columns
starting at desktops and scaling to large desktops
of various widths. Remember, grid columns should add up to twelve for a single horizontal block. More than that, and columns start stacking no matter the viewport.
.col-md-3
.col-md-6
.col-md-3
Two columns
Get two columns
starting at desktops and scaling to large desktops
.
.col-md-8
.col-md-4
Full width, single column
No grid classes are necessary for full-width elements.
Two columns with two nested columns
Per the documentation, nesting is easy—just put a row of columns within an existing column. This gives you two columns
starting at desktops and scaling to large desktops
, with another two (equal widths) within the larger column.
At mobile device sizes, tablets and down, these columns and their nested columns will stack.
.col-md-8
.col-md-6
.col-md-6
.col-md-4
Mixed: mobile and desktop
The Bootstrap v5 grid system has six tiers of classes: xs (extra small, this class infix is not used), sm (small), md (medium), lg (large), xl (x-large), and xxl (xx-large). You can use nearly any combination of these classes to create more dynamic and flexible layouts.
Each tier of classes scales up, meaning if you plan on setting the same widths for md, lg, xl and xxl, you only need to specify md.
.col-md-8
.col-6 .col-md-4
.col-6 .col-md-4
.col-6 .col-md-4
.col-6 .col-md-4
.col-6
.col-6
Mixed: mobile, tablet, and desktop
.col-sm-6 .col-lg-8
.col-6 .col-lg-4
.col-6 .col-sm-4
.col-6 .col-sm-4
.col-6 .col-sm-4
Gutters
With
.gx-*
classes, the horizontal gutters can be adjusted.
.col
with
.gx-4
gutters
.col
with
.gx-4
gutters
.col
with
.gx-4
gutters
.col
with
.gx-4
gutters
.col
with
.gx-4
gutters
.col
with
.gx-4
gutters
Use the
.gy-*
classes to control the vertical gutters.
.col
with
.gy-4
gutters
.col
with
.gy-4
gutters
.col
with
.gy-4
gutters
.col
with
.gy-4
gutters
.col
with
.gy-4
gutters
.col
with
.gy-4
gutters
With
.g-*
classes, the gutters in both directions can be adjusted.
.col
with
.g-3
gutters
.col
with
.g-3
gutters
.col
with
.g-3
gutters
.col
with
.g-3
gutters
.col
with
.g-3
gutters
.col
with
.g-3
gutters
Containers
Additional classes added in Bootstrap v4.4 allow containers that are 100% wide until a particular breakpoint. v5 adds a new
xxl
breakpoint.
.container
.container-sm
.container-md
.container-lg
.container-xl
.container-xxl
.container-fluid


## Cheatsheet · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/examples/cheatsheet/
- fetched_at: 2026-04-29T13:45:55.072842+00:00

Contents
Typography
Documentation
Display 1
Display 2
Display 3
Display 4
Display 5
Display 6
Heading 1
Heading 2
Heading 3
Heading 4
Heading 5
Heading 6
This is a lead paragraph. It stands out from regular paragraphs.
You can use the mark tag to
highlight
text.
This line of text is meant to be treated as deleted text.
This line of text is meant to be treated as no longer accurate.
This line of text is meant to be treated as an addition to the document.
This line of text will render as underlined.
This line of text is meant to be treated as fine print.
This line rendered as bold text.
This line rendered as italicized text.
A well-known quote, contained in a blockquote element.
This is a list.
It appears completely unstyled.
Structurally, it's still a list.
However, this style only applies to immediate child elements.
Nested lists:
are unaffected by this style
will still show a bullet
and have appropriate left margin
This may still come in handy in some situations.
This is a list item.
And another one.
But they're displayed inline.
Images
Documentation
Tables
Documentation
#
First
Last
Handle
1
Mark
Otto
@mdo
2
Jacob
Thornton
@fat
3
John
Doe
@social
#
First
Last
Handle
1
Mark
Otto
@mdo
2
Jacob
Thornton
@fat
3
John
Doe
@social
Class
Heading
Heading
Default
Cell
Cell
Primary
Cell
Cell
Secondary
Cell
Cell
Success
Cell
Cell
Danger
Cell
Cell
Warning
Cell
Cell
Info
Cell
Cell
Light
Cell
Cell
Dark
Cell
Cell
#
First
Last
Handle
1
Mark
Otto
@mdo
2
Jacob
Thornton
@fat
3
John
Doe
@social
Figures
Documentation
A caption for the above image.
Forms
Overview
Documentation
Disabled forms
Documentation
Sizing
Documentation
Open this select menu
One
Two
Three
Open this select menu
One
Two
Three
Input group
Documentation
@
@example.com
Your vanity URL
https://example.com/users/
$
.00
With textarea
Floating labels
Documentation
Validation
Documentation
Components
Accordion
Documentation
This is the first item's accordion body.
It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the
.accordion-body
, though the transition does limit overflow.
This is the second item's accordion body.
It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the
.accordion-body
, though the transition does limit overflow.
This is the third item's accordion body.
It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the
.accordion-body
, though the transition does limit overflow.
Alerts
Documentation
A simple primary alert with
an example link
. Give it a click if you like.
A simple secondary alert with
an example link
. Give it a click if you like.
A simple success alert with
an example link
. Give it a click if you like.
A simple danger alert with
an example link
. Give it a click if you like.
A simple warning alert with
an example link
. Give it a click if you like.
A simple info alert with
an example link
. Give it a click if you like.
A simple light alert with
an example link
. Give it a click if you like.
A simple dark alert with
an example link
. Give it a click if you like.
Well done!
Aww yeah, you successfully read this important alert message. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.
Whenever you need to, be sure to use margin utilities to keep things nice and tidy.
Badge
Documentation
Example heading
New
Example heading
New
Example heading
New
Example heading
New
Example heading
New
Example heading
New
Example heading
New
Example heading
New
Primary
Secondary
Success
Danger
Warning
Info
Light
Dark
Breadcrumb
Documentation
Buttons
Documentation
Button group
Documentation
Card
Documentation
Card title
Some quick example text to build on the card title and make up the bulk of the card's content.
Go somewhere
Featured
Card title
Some quick example text to build on the card title and make up the bulk of the card's content.
Go somewhere
2 days ago
Card title
Some quick example text to build on the card title and make up the bulk of the card's content.
An item
A second item
A third item
Card link
Another link
Card title
This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.
Last updated 3 mins ago
Carousel
Documentation
First slide label
Some representative placeholder content for the first slide.
Second slide label
Some representative placeholder content for the second slide.
Third slide label
Some representative placeholder content for the third slide.
Dropdowns
Documentation
Dropdown header
Action
Another action
Something else here
Separated link
Dropdown header
Action
Another action
Something else here
Separated link
Dropdown header
Action
Another action
Something else here
Separated link
Action
Another action
Something else here
Action
Another action
Something else here
Action
Another action
Something else here
Action
Another action
Something else here
Action
Another action
Something else here
Action
Another action
Something else here
Dropdown header
Action
Another action
Something else here
Separated link
Dropdown header
Action
Another action
Something else here
Separated link
Dropdown header
Action
Another action
Something else here
Separated link
Dropdown header
Action
Another action
Separated link
List group
Documentation
A disabled item
A second item
A third item
A fourth item
And a fifth one
An item
A second item
A third item
A fourth item
And a fifth one
A simple default list group item
A simple primary list group item
A simple secondary list group item
A simple success list group item
A simple danger list group item
A simple warning list group item
A simple info list group item
A simple light list group item
A simple dark list group item
Modal
Documentation
Navs
Documentation
This is some placeholder content the
Home tab's
associated content. Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to control the content visibility and styling. You can use it with tabs, pills, and any other
.nav
-powered navigation.
This is some placeholder content the
Profile tab's
associated content. Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to control the content visibility and styling. You can use it with tabs, pills, and any other
.nav
-powered navigation.
This is some placeholder content the
Contact tab's
associated content. Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to control the content visibility and styling. You can use it with tabs, pills, and any other
.nav
-powered navigation.
Active
Link
Link
Disabled
Navbar
Documentation
Pagination
Documentation
Popovers
Documentation
Progress
Documentation
0%
25%
50%
75%
100%
Scrollspy
Documentation
First heading
This is some placeholder content for the scrollspy page. Note that as you scroll down the page, the appropriate navigation link is highlighted. It's repeated throughout the component example. We keep adding some more example copy here to emphasize the scrolling and highlighting.
Second heading
This is some placeholder content for the scrollspy page. Note that as you scroll down the page, the appropriate navigation link is highlighted. It's repeated throughout the component example. We keep adding some more example copy here to emphasize the scrolling and highlighting.
Third heading
This is some placeholder content for the scrollspy page. Note that as you scroll down the page, the appropriate navigation link is highlighted. It's repeated throughout the component example. We keep adding some more example copy here to emphasize the scrolling and highlighting.
Fourth heading
This is some placeholder content for the scrollspy page. Note that as you scroll down the page, the appropriate navigation link is highlighted. It's repeated throughout the component example. We keep adding some more example copy here to emphasize the scrolling and highlighting.
Fifth heading
This is some placeholder content for the scrollspy page. Note that as you scroll down the page, the appropriate navigation link is highlighted. It's repeated throughout the component example. We keep adding some more example copy here to emphasize the scrolling and highlighting.
Spinners
Documentation
Loading...
Loading...
Loading...
Loading...
Loading...
Loading...
Loading...
Loading...
Loading...
Loading...
Loading...
Loading...
Loading...
Loading...
Loading...
Loading...
Toasts
Documentation
Bootstrap
11 mins ago
Hello, world! This is a toast message.
Tooltips
Documentation


## Navbar Template · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/examples/navbars/
- fetched_at: 2026-04-29T13:45:55.390364+00:00

Matching .container-xl...
Navbar examples
This example is a quick exercise to illustrate how the navbar and its contents work. Some navbars extend the width of the viewport, others are confined within a
.container
. For positioning of navbars, checkout the
top
and
fixed top
examples.
At the smallest breakpoint, the collapse plugin is used to hide the links and show a menu button to toggle the collapsed content.
View navbar docs »


## Navbar Template · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/examples/navbars-offcanvas/
- fetched_at: 2026-04-29T13:45:55.763877+00:00

Navbar with offcanvas examples
This example shows how responsive offcanvas menus work within the navbar. For positioning of navbars, checkout the
top
and
fixed top
examples.
From the top down, you'll see a dark navbar, light navbar and a responsive navbar—each with offcanvases built in. Resize your browser window to the large breakpoint to see the toggle for the offcanvas.
Learn more about offcanvas navbars »


## Offcanvas navbar template · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/examples/offcanvas-navbar/
- fetched_at: 2026-04-29T13:45:56.994499+00:00

Bootstrap
Since 2011
Recent updates
@username
Some representative placeholder content, with some information about this user. Imagine this being some sort of status update, perhaps?
@username
Some more representative placeholder content, related to this other user. Another status update, perhaps.
@username
This user also gets some representative placeholder content. Maybe they did something interesting, and you really want to highlight this in the recent updates.
All updates
Suggestions
Full Name
Follow
@username
Full Name
Follow
@username
Full Name
Follow
@username
All suggestions


## مثال الألبوم · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/examples/album-rtl/
- fetched_at: 2026-04-29T13:45:57.328019+00:00

مثال الألبوم
وصف قصير حول الألبوم أدناه (محتوياته ، ومنشؤه ، وما إلى ذلك). اجعله قصير ولطيف، ولكن ليست قصير جدًا حتى لا يتخطى الناس هذا الألبوم تمامًا.
الدعوة الرئيسية للعمل
عمل ثانوي
هذه بطاقة أوسع مع نص داعم أدناه كمقدمة طبيعية لمحتوى إضافي. هذا المحتوى أطول قليلاً.
9 دقائق
هذه بطاقة أوسع مع نص داعم أدناه كمقدمة طبيعية لمحتوى إضافي. هذا المحتوى أطول قليلاً.
9 دقائق
هذه بطاقة أوسع مع نص داعم أدناه كمقدمة طبيعية لمحتوى إضافي. هذا المحتوى أطول قليلاً.
9 دقائق
هذه بطاقة أوسع مع نص داعم أدناه كمقدمة طبيعية لمحتوى إضافي. هذا المحتوى أطول قليلاً.
9 دقائق
هذه بطاقة أوسع مع نص داعم أدناه كمقدمة طبيعية لمحتوى إضافي. هذا المحتوى أطول قليلاً.
9 دقائق
هذه بطاقة أوسع مع نص داعم أدناه كمقدمة طبيعية لمحتوى إضافي. هذا المحتوى أطول قليلاً.
9 دقائق
هذه بطاقة أوسع مع نص داعم أدناه كمقدمة طبيعية لمحتوى إضافي. هذا المحتوى أطول قليلاً.
9 دقائق
هذه بطاقة أوسع مع نص داعم أدناه كمقدمة طبيعية لمحتوى إضافي. هذا المحتوى أطول قليلاً.
9 دقائق
هذه بطاقة أوسع مع نص داعم أدناه كمقدمة طبيعية لمحتوى إضافي. هذا المحتوى أطول قليلاً.
9 دقائق


## مثال إتمام الشراء · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/examples/checkout-rtl/
- fetched_at: 2026-04-29T13:45:57.638539+00:00

نموذج إتمام الشراء
فيما يلي مثال على نموذج تم إنشاؤه بالكامل باستخدام عناصر تحكم النموذج في Bootstrap. لكل مجموعة نماذج مطلوبة حالة تحقق يمكن تشغيلها بمحاولة إرسال النموذج دون استكماله.
عربة التسوق
3
اسم المنتج
وصف مختصر
$12
المنتج الثاني
وصف مختصر
$8
البند الثالث
وصف مختصر
$5
رمز ترويجي
EXAMPLECODE
-$5
مجموع (USD)
$20
عنوان الفوترة


## قالب  شرائح العرض · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/examples/carousel-rtl/
- fetched_at: 2026-04-29T13:45:57.940049+00:00

عنوان المثال.
تشير الدراسات الإحصائية حسب الجمعية الأمريكية للغات بأن الإقبال على العربية زاد %126 في الولايات المتحدة الأمريكية وحدها بين عامي 2002 و2009م.
سجل اليوم
عنوان مثال آخر.
حسب المجلس الثقافي البريطاني فإن تعليم الإنجليزية داخل بريطانيا يسهم في تعزيز اقتصادها بما يتجاوز ملياري جنيه سنوياً، كما أنه وفر أكثر من 26 ألف وظيفة.
أعرف أكثر
واحد أكثر لقياس جيد.
الإحصاءات لحجم الاستثمار اللغوي خارج بريطانيا تتفاوت من سنة لأخرى إلا أن المدير التنفيذي للمجلس الثقافي البريطاني إدي بايرز يرى أن استثمار تعليم الإنجليزية في الخارج لا يحسب على المستوى المالي فحسب بل على المستوى السياسي أيضاً.
تصفح المعرض
عنوان
تذكر دائماً أن الحاسوب لا يمتلك ذكاءً، ولكنه يكتسب الذكاء الاصطناعي من خلال ثلاثة عناصر وظيفية رئيسة، هي: القدرة على التحليل، والقدرة على التأليف، والاستدلال المنطقي.
عرض التفاصيل
عنوان آخر
إذا أردنا استخدام الحاسوب الذكي في معالجة اللغة العربية فإننا نجد أنفسنا أمام تحدٍّ كبير، خاصة وأن لغتنا تمتاز بتماسك منظوماتها وتداخلها، ومع ذلك فإن الذكاء الاصطناعي يمكّننا من الحصول على أربعة أنواع من المعالجة، هي: المعالجة الصوتية، والمعالجة الصرفية، والمعالجة النحوية، والمعالجة الدلالية.
عرض التفاصيل
عنوان ثالث لتأكيد المعلومة
بفضل بحوث الذكاء الاصطناعي وتقنياته استطعنا الانتقال من مرحلة التعامل مع الفيزيائي إلى مرحلة التعامل مع المنطقي، وقد انعكس هذا الانتقال بصورة إيجابية على الكيفية التي تتعامل بها الشعوب مع لغاتها الحيَّة، وهذا يعني أنه يجب أن ينعكس بصورة إيجابية على كيفية تعاملنا مع لغتنا العربية.
عرض التفاصيل
العنوان الأول المميز.
سيذهل عقلك.
وجه الإنسان هو جزء معقَّد ومتميِّز للغاية من جسمه. وفي الواقع، إنه أحد أكثر أنظمة الإشارات المتاحة تعقيداً لدينا؛ فهو يتضمَّن أكثر من 40 عضلة مستقلة هيكلياً ووظيفياً، بحيث يمكن تشغيل كل منها بشكل مستقل عن البعض الآخر؛ وتشكِّل أحد أقوى مؤشرات العواطف.
أوه نعم، هذا جيد.
شاهد بنفسك.
عندما نضحك أو نبكي، فإننا نعرض عواطفنا، مما يسمح للآخرين بإلقاء نظرة خاطفة على أذهاننا أثناء "قراءة" وجوهنا بناءً على التغييرات في مكوّنات الوجه الرئيسة، مثل: العينين والحاجبين والجفنين والأنف والشفتين.
وأخيرًا، هذا.
كش ملك.
إن جميع العضلات في أجسامنا مدعمة بالأعصاب المتصلة من كافة أنحاء الجسم بالنخاع الشوكي والدماغ. وهذا الاتصال العصبي هو ثنائي الاتجاه، أي إن العصب يتسبَّب في تقلصات العضلات بناءً على إشارات الدماغ، ويقوم في الوقت نفسه بإرسال معلومات عن حالة العضلات إلى الدماغ


## قالب المدونة · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/examples/blog-rtl/
- fetched_at: 2026-04-29T13:45:58.346560+00:00

عنوان تدوينة مميزة أطول
عدة أسطر نصية متعددة تعبر عن التدوية، وذلك لإعلام القراء الجدد بسرعة وكفاءة حول أكثر الأشياء إثارة للاهتمام في محتويات هذه التدوينة.
أكمل القراءة...
العالم
مشاركة مميزة
نوفمبر 12
هذه بطاقة أوسع مع نص داعم أدناه كمقدمة طبيعية لمحتوى إضافي.
أكمل القراءة
التصميم
عنوان الوظيفة
نوفمبر 11
هذه بطاقة أوسع مع نص داعم أدناه كمقدمة طبيعية لمحتوى إضافي.
أكمل القراءة
من Firehose
مثال على تدوينة
1 يناير 2021 بواسطة
Mark
تعرض مشاركة المدونة هذه بضعة أنواع مختلفة من المحتوى الذي يتم دعمه وتصميمه باستخدام Bootstrap. النصوص الأساسية، الصور، والأكواد مدعومة بشكل كامل.
يشكِّل تأمين الغذاء في المستقبل قضية تؤرِّق حكومات العالَم والعلماء على حدٍّ سواء. فخلال القرن العشرين ازداد عدد سكان الأرض أربعة أضعاف، وتشير التقديرات إلى أن العدد سوف يصل إلى عشرة مليارات إنسان بحلول عام 2050م. وسوف تمثل هذه الزيادة الهائلة تحدياً كبيراً وضغطاً متصاعداً على قدرة الإنتاج الزراعي. الأمر الذي كان ولا بد من أن يدفع إلى تطوير تقنيات مبتكرة في تصنيع الغذاء غير الزراعة، منها تقنية مستقبلية تقوم على تصنيع الغذاء من الهواء.
تشغل الزراعة مساحات كبيرة من اليابسة، وتستهلك كميات هائلة من المياه، كما أن إنتاج الغذاء بواسطة الزراعة يسهم بنسبة عالية من انبعاثات غازات الاحتباس الحراري العالمية
تشغل الزراعة مساحات كبيرة من اليابسة، وتستهلك كميات هائلة من المياه. كما أن إنتاج الغذاء بواسطة الزراعة يسهم بنسبة عالية من انبعاثات غازات الاحتباس الحراري العالمية، وللمقارنة فإن هذه النسبة من الانبعاثات هي أكبر مما ينتجه قطاع النقل بكل ما فيه من سيارات وشاحنات وطائرات وقطارات.
عنوان
تحصل النباتات على غذائها بواسطة عملية تسمى البناء الضوئي، حيث تقوم النباتات بتحويل ضوء الشمس والماء وثاني أكسيد الكربون الموجود في الغلاف الجوي إلى غذاء وتطلق الأكسجين كمنتج ثانوي لهذا التفاعل الكيميائي. وتحدث هذه العملية في "البلاستيدات الخضراء". فالنباتات تستفيد من طاقة ضوء الشمس في تقسيم الماء إلى هيدروجين وأكسجين، وتحدث تفاعلات كيميائية أخرى ينتج عنها سكر الجلكوز الذي تستخدمه كمصدر للغذاء وينطلق الأكسجين من النباتات إلى الغلاف الجوي. وهذا يعني أن النباتات تحوِّل ثاني أكسيد الكربون إلى غذاء من خلال تفاعلات كيميائية معقَّدة. ويُعد البناء الضوئي من أهم التفاعلات الكيميائية على كوكب الأرض، فقد ساعد في الماضي على تطوُّر كوكبنا وظهور الحياة عليه. فالنباتات تستخدم ثاني أكسيد الكربون لصنع غذائها، وتطلق الأكسجين لتساعد الكائنات الأخرى على التنفس!
عنوان فرعي
ألهمت هذه العملية علماء وكالة الفضاء الأمريكية (ناسا) خلال الستينيات من القرن الماضي، لبحث فكرة إطعام روَّاد الفضاء في مهمات الفضاء الطويلة مثل السفر إلى المريخ. وكانت واحدة من الأفكار الواعدة تصنيع الغذاء عن طريق ثاني أكسيد الكربون الذي ينتجه روَّاد الفضاء، لكن ليس بواسطة النباتات بل عن طريق ميكروبات صغيرة وحيدة الخلية قادرة على حصد ثاني أكسيد الكربون لإنتاج كميات وفيرة من البروتين المغذي على شكل مسحوق عديم النكهة، كما يمكن استخدام المادة في صنع الأطعمة المألوفة لدينا.
Example code block
وخلافاً لما هو الحال في عالم النبات، فإن هذه الميكروبات لا تستخدم الضوء كما يحدث في عملية البناء الضوئي التي تستخدمها النباتات للحصول على الغذاء، أي لأنها قادرة على النمو في الظلام. تسمى هذه البكتريا "هيدروجينوتروف" (Hydrogenotrophs)، وهي تستخدم الهيدروجين كوقود لإنتاج الغذاء من ثاني أكسيد الكربون. فعندما يُنتج روَّاد الفضاء ثاني أكسيد الكربون، تلتقطه الميكروبات، ويتحوَّل مع مدخلات أخرى إلى غذاء غني بالكربون. وبهذه الطريقة سوف نحصل على دورة كربون مغلقة الحلقة.
عنوان فرعي
بعد مرور أكثر من نصف قرن على أبحاث ناسا، تعمل حالياً عدة شركات في قطاع البيولوجيا التركيبية من ضمنها إير بروتين (Air Protein) وسولار فودز (Solar Foods) على تطوير جيل جديد من المنتجات الغذائية المستدامة، من دون وجود بصمة كربونية. ولن تقتصر هذه المنتجات الغذائية على روَّاد الفضاء فحسب، بل سوف تمتد لتشمل جميع سكان الأرض، وسوف تُنتَج في فترة زمنية قصيرة، بدلاً من الشهور، ومن دون الاعتماد على الأراضي الزراعية. وهذا يعني الحصول على منتجات غذائية بشكل سريع جداً. كما سيصبح من الممكن تصنيع الغذاء بطريقة عمودية من خلال هذه الميكروبات، بدلاً من الطريقة الأفقية التقليدية الشبيهة بتقنية الزراعة العمودية الحديثة. وهذا يعني توفير منتجات غذائية أكبر من المساحة نفسها.
يتكوَّن الغذاء البشري من ثلاثة أنواع رئيسة، هي:
البروتينات
الكربوهيدرات
الدهون
وتتكوَّن البروتينات من الأحماض الأمينية، وهي مجموعة من المركبات العضوية يبلغ عددها في جسم الإنسان عشرين حمضاً أمينياً، من بينها تسعة أساسية يحصل عليها الجسم من الغذاء. وتتكوَّن الأحماض الأمينية بشكل أساس من:
الكربون
الهيدروجين
الأكسجين
النيتروجين
ومن الملاحظ أن النيتروجين يشكِّل نسبة %78 من الهواء، كما أن الهيدروجين نحصل عليه من خلال التحليل الكهربائي للماء، ومن الممكن نظرياً سحب الكربون من الهواء لتشكيل هذه الأحماض، ذلك أن الكربون هو العمود الفقري للأحماض الأمينية، كما أن الحياة على كوكب الأرض قائمة على الكربون لقدرته على تكوين سلاسل كربونية طويلة، وهذا ما تفعله الميكروبات بتصنيع أحماض أمينية من ثاني أكسيد الكربون من خلال مجموعة من التفاعلات الكيميائية المعقَّدة. وإضافة إلى صنع وجبات غنية بالبروتين، فهذه الميكروبات تنتج منتجات أخرى مثل الزيوت التي لها عديد من الاستخدامات.
تدوينة أخرى
23 ديسمبر 2020 بواسطة
Jacob
في الوقت الحالي، تدرس عدَّة شركات هذه الميكروبات بشكل أعمق، وتستزرعها من أجل الحصول على الغذاء. ففي عام 2019م، أعلن باحثون في شركة (Air Protein) الأمريكية نجاحهم في تحويل ثاني أكسيد الكربون الموجود في الهواء إلى لحوم صناعية مصنوعة من البروتين، التي لا تتطلَّب أي أرض زراعية، بل هي معتمدة بشكل أساسي على الهواء.
تم تصنيع اللحوم بأنواع عديدة
إذ استخدم هؤلاء الباحثون الهواء والطاقة المتجدِّدة كمدخلات في عملية مشابهة للتخمير، لإنتاج بروتين يحتوي على الأحماض الأمينية التسعة الأساسية وغني بالفيتامينات والمعادن، كما أنه خالٍ من الهرمونات والمضادات الحيوية والمبيدات الحشرية ومبيدات الأعشاب.
وتم تصنيع اللحوم بأنواع عديدة بما فيها الدواجن والأبقار والمأكولات البحرية، من دون حصول انبعاثات كربونية، على عكس تربية الأبقار التي تسهم في انبعاث غاز الميثان أحد غازات الاحتباس الحراري.
ميزة جديدة
14 ديسمبر 2020 بواسطة
Jacob
كما أن الشركة الفنلندية (Solar Foods) طوَّرت تقنية لإنتاج البروتين من الهواء، حيث تبدأ العملية بتقسيم الماء إلى مكوناته الهيدروجين والأكسجين عن طريق الكهرباء. فالهيدروجين يوفِّر الطاقة للبكتريا لتحويل ثاني أكسيد الكربون والنيتروجين الموجودين في الهواء إلى مادة عضوية غنية بالبروتين بشكل أكفأ من نمو النباتات باستخدام البناء الضوئي. وهذا البروتين يشبه دقيق القمح وقد أطلق عليه اسم "سولين" (Solein).
وتقوم الشركة حالياً بجمع البيانات حول المنتج الغذائي لتقديمه إلى الاتحاد الأوروبي بهدف الحصول على ترخيص غذائي، كما أنها تخطط لبدء الإنتاج التجاري في العام المقبل 2021م. وقد أوضحت الشركة أنها مهتمة بإنتاج أطعمة صديقة للبيئة من خلال استخدام المواد الأساسية: الكهرباء وثاني أكسيد الكربون، وهذه الأطعمة سوف تجنبنا الأثر السلبي البيئي للزراعة التقليدية الذي يشمل كل شيء من استخدام الأرض والمياه إلى الانبعاثات الناتجة من تسميد المحاصيل أو تربية الحيوانات.
وعلى هذا، فإن البروتينات المشتقة من الميكروبات سوف:
توفر حلاً ممكناً في ظل زيادة الطلب العالمي المستقبلي على الغذاء
تتوسع مصانع الغذاء في المستقبل لتكون أكفأ وأكثر استدامة
تصبح قادرة على توفير الغذاء لروَّاد الفضاء في سفرهم إلى المريخ وجميع سكان كوكب الأرض في عام 2050م
فتخيّل أن الميكروبات ستكون مصانع المستقبل، وأن غذاء المستقبل سيكون مصنوعاً من الهواء! وأن عام 2050م سيكون مختلفاً تماماً عن عالمنا اليوم. فهو عالم من دون زراعة ولا تربية حيوانات من أجل الغذاء! قد يبدو ذلك خيالياً لكنه ليس مستحيلاً!
حول
أقبلت، فأقبلت معك الحياة بجميع صنوفها وألوانها: فالنبات ينبت، والأشجار تورق وتزهر، والهرة تموء، والقمري يسجع، والغنم يثغو، والبقر يخور، وكل أليف يدعو أليفه. كل شيء يشعر بالحياة وينسي هموم الحياة، ولا يذكر إلا سعادة الحياة، فإن كان الزمان جسدا فأنت روحه، وإن كان عمرا فأنت شبابه.
المشاركات الاخيرة
مثال على عنوان منشور المدونة
15 يناير 2024
هذا عنوان آخر للمدونة
14 يناير 2024
أطول عنوان منشور للمدونة: يحتوي هذا الخط على عدة أسطر!
13 يناير 2024
الأرشيف
مارس 2021
شباط 2021
يناير 2021
ديسمبر 2020
نوفمبر 2020
أكتوبر 2020
سبتمبر 2020
اغسطس 2020
يوليو 2020
يونيو 2020
مايو 2020
ابريل 2020
في مكان آخر
GitHub
Social
Facebook


## قالب لوحة القيادة · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/examples/dashboard-rtl/
- fetched_at: 2026-04-29T13:45:58.673070+00:00

لوحة القيادة
عنوان القسم
#
عنوان
عنوان
عنوان
عنوان
1,001
بيانات
عشوائية
تثري
الجدول
1,002
تثري
مبهة
تصميم
تنسيق
1,003
عشوائية
غنية
قيمة
مفيدة
1,003
معلومات
تثري
توضيحية
عشوائية
1,004
الجدول
بيانات
تنسيق
قيمة
1,005
قيمة
مبهة
الجدول
تثري
1,006
قيمة
توضيحية
غنية
عشوائية
1,007
تثري
مفيدة
معلومات
مبهة
1,008
بيانات
عشوائية
تثري
الجدول
1,009
تثري
مبهة
تصميم
تنسيق
1,010
عشوائية
غنية
قيمة
مفيدة
1,011
معلومات
تثري
توضيحية
عشوائية
1,012
الجدول
تثري
تنسيق
قيمة
1,013
قيمة
مبهة
الجدول
تصميم
1,014
قيمة
توضيحية
غنية
عشوائية
1,015
بيانات
مفيدة
معلومات
الجدول


## ورقة الغش · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/examples/cheatsheet-rtl/
- fetched_at: 2026-04-29T13:45:59.052194+00:00

المحتوى
النصوص
دليل الإستخدام
العرض 1
العرض 2
العرض 3
العرض 4
العرض 5
العرض 6
عنوان 1
عنوان 2
عنوان 3
عنوان 4
عنوان 5
عنوان 6
هذه قطعة إملائية متميزة، فهي مصممة لتكون بارزة من بين القطع الإملائية الأخرى.
يمكنك استخدام تصنيف mark
لتحديد
نص.
من المفترض أن يتم التعامل مع هذا السطر كنص محذوف.
من المفترض أن يتم التعامل مع هذا السطر على أنه لم يعد دقيقًا.
من المفترض أن يتم التعامل مع هذا السطر كإضافة إلى المستند.
سيتم عرض النص في هذا السطر كما وتحته خط.
من المفترض أن يتم التعامل مع هذا السطر على أنه يحوي تفاصيل صغيرة.
هذا السطر يحوي نص عريض.
هذا السطر يحوي نص مائل.
إقتباس مبهر، موضوع في عنصر blockquote
هذه قائمة عناصر.
بالرغم من أنها مصممة كي لا تظهر كذلك.
إلا أنها مجهزة كـ قائمة خلف الكواليس
هذا التصميم ينطبق فقد على القائمة الرئيسية
القوائم الفرعية
لا تتأثر بهذا التصميم
فهي تظهر عليها علامات الترقيم
وتحتوي على مساحة فارغة بجوارها
قد يكون هذا التصميم مفيدًا في بعض الأحيان.
هذا عنصر في قائمة.
وهذا أيضًا.
لكنهم يظهرون متجاورين.
الصور
دليل الإستخدام
الجداول
دليل الإستخدام
#
الاسم الاول
الكنية
الاسم المستعار
1
Mark
Otto
@mdo
2
Jacob
Thornton
@fat
3
John
Doe
@social
#
الاسم الاول
الكنية
الاسم المستعار
1
Mark
Otto
@mdo
2
Jacob
Thornton
@fat
3
John
Doe
@social
Class
عنوان
عنوان
Default
خلية
خلية
Primary
خلية
خلية
Secondary
خلية
خلية
Success
خلية
خلية
Danger
خلية
خلية
Warning
خلية
خلية
Info
خلية
خلية
Light
خلية
خلية
Dark
خلية
خلية
#
الاسم الاول
الكنية
الاسم المستعار
1
Mark
Otto
@mdo
2
Jacob
Thornton
@fat
3
John
Doe
@social
النماذج البيانية
دليل الإستخدام
شرح للصورة أعلاه.
النماذج
نظرة عامة
دليل الإستخدام
الحقول المعطلة
دليل الإستخدام
الأحجام
دليل الإستخدام
افتح قائمة الاختيار هذه
واحد
اثنان
ثلاثة
افتح قائمة الاختيار هذه
واحد
اثنان
ثلاثة
مجموعة الإدخال
دليل الإستخدام
أنا اسمي
وغيرها
عنوان حسابك الشخصي
https://example.com/users/
.00
$
مع textarea
الحقول ذوي العناوين العائمة
دليل الإستخدام
التحقق
دليل الإستخدام
العناصر
المطوية
دليل الإستخدام
هذا هو محتوى عنصر المطوية الأول.
سيكون المحتوى مخفيًا بشكل إفتراضي حتى يقوم Bootstrap بإضافة الكلاسات اللازمة لكل عنصر في المطوية. هذه الكلاسات تتحكم بالمظهر العام ووتتحكم أيضا بإظهار وإخفاء أقسام المطوية عبر حركات CSS الإنتقالية. يمكنك تعديل أي من هذه عبر كلاسات CSS خاصة بك، او عبر تغيير القيم الإفتراضية المقدمة من Bootstrap. من الجدير بالذكر أنه يمكن وضع أي كود HTML هنا، ولكن الحركة الإنتقالية قد تحد من الoverflow.
هذا هو محتوى عنصر المطوية الثاني.
سيكون المحتوى مخفيًا بشكل إفتراضي حتى يقوم Bootstrap بإضافة الكلاسات اللازمة لكل عنصر في المطوية. هذه الكلاسات تتحكم بالمظهر العام ووتتحكم أيضا بإظهار وإخفاء أقسام المطوية عبر حركات CSS الإنتقالية. يمكنك تعديل أي من هذه عبر كلاسات CSS خاصة بك، او عبر تغيير القيم الإفتراضية المقدمة من Bootstrap. من الجدير بالذكر أنه يمكن وضع أي كود HTML هنا، ولكن الحركة الإنتقالية قد تحد من الoverflow.
هذا هو محتوى عنصر المطوية الثالث.
سيكون المحتوى مخفيًا بشكل إفتراضي حتى يقوم Bootstrap بإضافة الكلاسات اللازمة لكل عنصر في المطوية. هذه الكلاسات تتحكم بالمظهر العام ووتتحكم أيضا بإظهار وإخفاء أقسام المطوية عبر حركات CSS الإنتقالية. يمكنك تعديل أي من هذه عبر كلاسات CSS خاصة بك، او عبر تغيير القيم الإفتراضية المقدمة من Bootstrap. من الجدير بالذكر أنه يمكن وضع أي كود HTML هنا، ولكن الحركة الإنتقالية قد تحد من الoverflow.
الإنذارات
دليل الإستخدام
تنبيه primary بسيط مع
رابط مثال
. أعطها نقرة إذا أردت.
تنبيه secondary بسيط مع
رابط مثال
. أعطها نقرة إذا أردت.
تنبيه success بسيط مع
رابط مثال
. أعطها نقرة إذا أردت.
تنبيه danger بسيط مع
رابط مثال
. أعطها نقرة إذا أردت.
تنبيه warning بسيط مع
رابط مثال
. أعطها نقرة إذا أردت.
تنبيه info بسيط مع
رابط مثال
. أعطها نقرة إذا أردت.
تنبيه light بسيط مع
رابط مثال
. أعطها نقرة إذا أردت.
تنبيه dark بسيط مع
رابط مثال
. أعطها نقرة إذا أردت.
أحسنت!
لقد نجحت في قراءة رسالة التنبيه المهمة هذه. سيتم تشغيل نص المثال هذا لفترة أطول قليلاً حتى تتمكن من رؤية كيفية عمل التباعد داخل التنبيه مع هذا النوع من المحتوى.
كلما احتجت إلى ذلك ، تأكد من استخدام أدوات الهامش للحفاظ على الأشياء لطيفة ومرتبة.
الشارة
دليل الإستخدام
مثال على عنوان
جديد
مثال على عنوان
جديد
مثال على عنوان
جديد
مثال على عنوان
جديد
مثال على عنوان
جديد
مثال على عنوان
جديد
مثال على عنوان
جديد
مثال على عنوان
جديد
Primary
Secondary
Success
Danger
Warning
Info
Light
Dark
مسار التنقل التفصيلي (فتات الخبز)
دليل الإستخدام
الأزرار
دليل الإستخدام
مجموعة الأزرار
دليل الإستخدام
البطاقة
دليل الإستخدام
عنوان البطاقة
بعض الأمثلة السريعة للنصوص للبناء على عنوان البطاقة وتشكيل الجزء الأكبر من محتوى البطاقة.
اذهب لمكان ما
متميز
عنوان البطاقة
بعض الأمثلة السريعة للنصوص للبناء على عنوان البطاقة وتشكيل الجزء الأكبر من محتوى البطاقة.
اذهب لمكان ما
منذ يومان
عنوان البطاقة
بعض الأمثلة السريعة للنصوص للبناء على عنوان البطاقة وتشكيل الجزء الأكبر من محتوى البطاقة.
عنصر
عنصر آخر
عنصر ثالث
رابط البطاقة
رابط آخر
عنوان البطاقة
هذه بطاقة أعرض مع نص داعم تحتها كمقدمة طبيعية لمحتوى إضافي. هذا المحتوى أطول قليلاً.
آخر تحديث منذ 3 دقائق
شرائح العرض
دليل الإستخدام
عنوان الشريحة الأولى
محتوى وصفي يعبئ فراغ الشريحة الأولى.
عنوان الشريحة الثانية
محتوى وصفي يعبئ فراغ الشريحة الأولى.
عنوان الشريحة الثالثة
محتوى وصفي يعبئ فراغ الشريحة الأولى.
القوائم المنسدلة
دليل الإستخدام
عنوان القائمة المنسدلة
عمل
عمل آخر
شيء آخر هنا
رابط منفصل
عنوان القائمة المنسدلة
عمل
عمل آخر
شيء آخر هنا
رابط منفصل
عنوان القائمة المنسدلة
عمل
عمل آخر
شيء آخر هنا
رابط منفصل
عمل
عمل آخر
شيء آخر هنا
عمل
عمل آخر
شيء آخر هنا
عمل
عمل آخر
شيء آخر هنا
عمل
عمل آخر
شيء آخر هنا
عمل
عمل آخر
شيء آخر هنا
عمل
عمل آخر
شيء آخر هنا
عنوان القائمة المنسدلة
عمل
عمل آخر
شيء آخر هنا
رابط منفصل
عنوان القائمة المنسدلة
عمل
عمل آخر
شيء آخر هنا
رابط منفصل
عنوان القائمة المنسدلة
عمل
عمل آخر
شيء آخر هنا
رابط منفصل
عنوان القائمة المنسدلة
عمل
عمل آخر
رابط منفصل
مجموعة العناصر
دليل الإستخدام
عنصر معطل
عنصر ثاني
عنصر ثالث
عنصر رابع
وعنصر خامس أيضًا
عنصر
عنصر ثاني
عنصر ثالث
عنصر رابع
وعنصر خامس أيضًا
عنصر مجموعة قائمة default بسيط
عنصر مجموعة قائمة primary بسيط
عنصر مجموعة قائمة secondary بسيط
عنصر مجموعة قائمة success بسيط
عنصر مجموعة قائمة danger بسيط
عنصر مجموعة قائمة warning بسيط
عنصر مجموعة قائمة info بسيط
عنصر مجموعة قائمة light بسيط
عنصر مجموعة قائمة dark بسيط
الصندوق العائم
دليل الإستخدام
التنقل
دليل الإستخدام
محتوى لتوضيح كيف يعمل التبويب. هذا المحتوى مرتبط بتبويب الصفحة الرئيسية. إذن، أمامنا بعض التحدّيات الصعبة. لكن لا يمكننا أن نعتمد على التطورات التكنولوجية وحدها في ميدان قوى السوق الحرة، لإخراجنا من هذه الورطة، لا سيّما أنها نفسها، مقرونة بالافتقار إلى البصيرة، هي التي أودت بنا إلى هذا التبدُّل المناخي في الدرجة الأولى.
محتوى لتوضيح كيف يعمل التبويب. هذا المحتوى مرتبط بتبويب الملف الشخصي. معظم البشر في بلدان العالَم النامي، لم يقتنوا بعد مكيّفهم الأول، والمشكلة إلى ازدياد. فمعظم البلدان النامية هي من البلدان الأشد حرارة والأكثر اكتظاظًا بالسكان في العالم.
محتوى لتوضيح كيف يعمل التبويب. هذا المحتوى مرتبط بتبويب الاتصال بنا. أمامنا بعض التحدّيات الصعبة. لكن لا يمكننا أن نعتمد على التطورات التكنولوجية وحدها في ميدان قوى السوق الحرة، بل يجب وضع معايير جدوى جديدة لشركات البناء ومعايير أعلى لجدوى التكييف من أجل تحفيز الحلول المستدامة قانونيًا.
نشط
رابط
رابط
معطل
شريط التنقل
دليل الإستخدام
ترقيم الصفحات
دليل الإستخدام
الصناديق المنبثقة
دليل الإستخدام
شريط التقدم
دليل الإستخدام
0%
25%
50%
75%
100%
المخطوطة
دليل الإستخدام
@fat
محتوى لتوضيح كيف تعمل المخطوطة. ببساطة، المخطوطة عبارة عن منشور طويل يحتوي على عدة أقسام، ولديه شريط تنقل يسهل الوصول إلى هذه الأقسام الفرعية.
@mdo
بصرف النظر عن تحسيننا جدوى المكيّفات أو عدم تحسينها، فإن الطلب على الطاقة سيزداد. وطبقاً لما جاء في مقالة معهد ماساشوستس للتكنولوجيا، السالف ذكره، ثمَّة أمر يجب عدم إغفاله، وهو كيف أن هذا الطلب سيضغط على نظم توفير الطاقة الحالية. إذ لا بد من إعادة تأهيل كل شبكات الكهرباء، وتوسيعها لتلبية طلب الطاقة في زمن الذروة، خلال موجات الحرارة المتزايدة. فحين يكون الحر شديداً يجنح الناس إلى البقاء في الداخل، وإلى زيادة تشغيل المكيّفات، سعياً إلى جو لطيف وهم يستخدمون أدوات وأجهزة مختلفة أخرى.
واحد
وكل هذه الأمور المتزامنة من تشغيل الأجهزة، يزيد الضغط على شبكات الطاقة، كما أسلفنا. لكن مجرد زيادة سعة الشبكة ليس كافياً. إذ لا بد من تطوير الشبكات الذكية التي تستخدم الجسّاسات، ونظم المراقبة، والبرامج الإلكترونية، لتحديد متى يكون الشاغلون في المبنى، ومتى يكون ثمَّة حاجة إلى الطاقة، ومتى تكون الحرارة منخفضة، وبذلك يخرج الناس، فلا يستخدمون كثيراً من الكهرباء.
اثنان
مع الأسف، كل هذه الحلول المبتكرة مكلِّفة، وهذا ما يجعلها عديمة الجدوى في نظر بعض الشركات الخاصة والمواطن المتقشّف. إن بعض الأفراد الواعين بيئياً يبذلون قصارى جهدهم في تقليص استهلاكهم من الطاقة، ويعون جيداً أهمية أجهزة التكييف المجدية والأرفق بالبيئة. ولكن جهات كثيرة لن تتحرّك لمجرد حافز سلامة المناخ ووقف هدر الطاقة، ما دامت لا تحركها حوافز قانونية. وعلى الحكومات أن تُقدِم عند الاهتمام بالتغيّر المناخي، على وضع التشريعات المناسبة. فبالنظم والحوافز والدعم، يمكن دفع الشركات إلى اعتماد الحلول الأجدى في مكاتبها.
ثلاثة
وكما يتبيّن لنا، من عدد الحلول الملطِّفة للمشكلة، ومن تنوّعها، وهي الحلول التي أسلفنا الحديث عنها، فإن التكنولوجيا التي نحتاج إليها من أجل معالجة هذه التحديات، هي في مدى قدرتنا، لكنها ربما تتطلّب بعض التحسين، ودعماً استثمارياً أكبر!
ولا مانع من إضافة محتوى آخر ليس تحت أي قسم معين.
الدوائر المتحركة
دليل الإستخدام
جار التحميل...
جار التحميل...
جار التحميل...
جار التحميل...
جار التحميل...
جار التحميل...
جار التحميل...
جار التحميل...
جار التحميل...
جار التحميل...
جار التحميل...
جار التحميل...
جار التحميل...
جار التحميل...
جار التحميل...
جار التحميل...
الإشعارات
دليل الإستخدام
Bootstrap
قبل 11 دقيقة
مرحبًا بالعالم! هذه رسالة إشعار.
التلميحات
دليل الإستخدام


## Masonry example · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/examples/masonry/
- fetched_at: 2026-04-29T13:45:59.360701+00:00

Bootstrap and Masonry
Integrate
Masonry
with the Bootstrap grid system and cards component.
Masonry is not included in Bootstrap. Add it by including the JavaScript plugin manually, or using a CDN like so:
<script src="https://cdn.jsdelivr.net/npm/masonry-layout@4.2.2/dist/masonry.pkgd.min.js" integrity="sha384-GNFwBvfVxBkLMJpYMOABq3c+d3KnQxudP/mGPkzpZSTYykLBNsZEnG2D9G/X/+7D" crossorigin="anonymous" async></script>
By adding
data-masonry='{"percentPosition": true }'
to the
.row
wrapper, we can combine the powers of Bootstrap's responsive grid and Masonry's positioning.
Card title that wraps to a new line
This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.
A well-known quote, contained in a blockquote element.
Someone famous in
Source Title
Card title
This card has supporting text below as a natural lead-in to additional content.
Last updated 3 mins ago
A well-known quote, contained in a blockquote element.
Someone famous in
Source Title
Card title
This card has a regular title and short paragraph of text below it.
Last updated 3 mins ago
A well-known quote, contained in a blockquote element.
Someone famous in
Source Title
Card title
This is another card with title and supporting text below. This card has some additional content to make it slightly taller overall.
Last updated 3 mins ago


## Placeholders · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/components/placeholders/
- fetched_at: 2026-04-29T13:45:59.552224+00:00

Added in v5.1
View on GitHub
Placeholders
Use loading placeholders (skeleton loaders) for your components or pages to indicate something may still be loading.
On this page
About
Placeholders can be used to enhance the experience of your application. They’re built only with HTML and CSS, meaning you don’t need any JavaScript to create them. You will, however, need some custom JavaScript to toggle their visibility. Their appearance, color, and sizing can be easily customized with our utility classes.
Example
In the example below, we take a typical card component and recreate it with placeholders applied to create a “loading card”. Size and proportions are the same between the two.
Card title
Some quick example text to build on the card title and make up the bulk of the card’s content.
Go somewhere
<
div
class
=
"
card
"
>
<
img
src
=
"
...
"
class
=
"
card-img-top
"
alt
=
"
...
"
>
<
div
class
=
"
card-body
"
>
<
h5
class
=
"
card-title
"
>
Card title
</
h5
>
<
p
class
=
"
card-text
"
>
Some quick example text to build on the card title and make up the bulk of the card’s content.
</
p
>
<
a
href
=
"
#
"
class
=
"
btn btn-primary
"
>
Go somewhere
</
a
>
</
div
>
</
div
>
<
div
class
=
"
card
"
aria-hidden
=
"
true
"
>
<
img
src
=
"
...
"
class
=
"
card-img-top
"
alt
=
"
...
"
>
<
div
class
=
"
card-body
"
>
<
h5
class
=
"
card-title placeholder-glow
"
>
<
span
class
=
"
placeholder col-6
"
>
</
span
>
</
h5
>
<
p
class
=
"
card-text placeholder-glow
"
>
<
span
class
=
"
placeholder col-7
"
>
</
span
>
<
span
class
=
"
placeholder col-4
"
>
</
span
>
<
span
class
=
"
placeholder col-4
"
>
</
span
>
<
span
class
=
"
placeholder col-6
"
>
</
span
>
<
span
class
=
"
placeholder col-8
"
>
</
span
>
</
p
>
<
a
class
=
"
btn btn-primary disabled placeholder col-6
"
aria-disabled
=
"
true
"
>
</
a
>
</
div
>
</
div
>
How it works
Create placeholders with the
.placeholder
class and a grid column class (e.g.,
.col-6
) to set the
width
. They can replace the text inside an element or be added as a modifier class to an existing component.
We apply additional styling to
.btn
s via
::before
to ensure the
height
is respected. You may extend this pattern for other situations as needed, or add a
&nbsp;
within the element to reflect the height when actual text is rendered in its place.
html
<
p
aria-hidden
=
"
true
"
>
<
span
class
=
"
placeholder col-6
"
>
</
span
>
</
p
>
<
a
class
=
"
btn btn-primary disabled placeholder col-4
"
aria-disabled
=
"
true
"
>
</
a
>
The use of
aria-hidden="true"
only indicates that the element should be hidden to screen readers. The
loading
behavior of the placeholder depends on how authors will actually use the placeholder styles, how they plan to update things, etc. Some JavaScript code may be needed to
swap
the state of the placeholder and inform AT users of the update.
Width
You can change the
width
through grid column classes, width utilities, or inline styles.
html
<
span
class
=
"
placeholder col-6
"
>
</
span
>
<
span
class
=
"
placeholder w-75
"
>
</
span
>
<
span
class
=
"
placeholder
"
style
=
"
width
:
25%
;
"
>
</
span
>
Color
By default, the
placeholder
uses
currentColor
. This can be overridden with a custom color or utility class.
html
<
span
class
=
"
placeholder col-12
"
>
</
span
>
<
span
class
=
"
placeholder col-12 bg-primary
"
>
</
span
>
<
span
class
=
"
placeholder col-12 bg-secondary
"
>
</
span
>
<
span
class
=
"
placeholder col-12 bg-success
"
>
</
span
>
<
span
class
=
"
placeholder col-12 bg-danger
"
>
</
span
>
<
span
class
=
"
placeholder col-12 bg-warning
"
>
</
span
>
<
span
class
=
"
placeholder col-12 bg-info
"
>
</
span
>
<
span
class
=
"
placeholder col-12 bg-light
"
>
</
span
>
<
span
class
=
"
placeholder col-12 bg-dark
"
>
</
span
>
Sizing
The size of
.placeholder
s are based on the typographic style of the parent element. Customize them with sizing modifiers:
.placeholder-lg
,
.placeholder-sm
, or
.placeholder-xs
.
html
<
span
class
=
"
placeholder col-12 placeholder-lg
"
>
</
span
>
<
span
class
=
"
placeholder col-12
"
>
</
span
>
<
span
class
=
"
placeholder col-12 placeholder-sm
"
>
</
span
>
<
span
class
=
"
placeholder col-12 placeholder-xs
"
>
</
span
>
Animation
Animate placeholders with
.placeholder-glow
or
.placeholder-wave
to better convey the perception of something being
actively
loaded.
html
<
p
class
=
"
placeholder-glow
"
>
<
span
class
=
"
placeholder col-12
"
>
</
span
>
</
p
>
<
p
class
=
"
placeholder-wave
"
>
<
span
class
=
"
placeholder col-12
"
>
</
span
>
</
p
>
CSS
Sass variables
scss/_variables.scss
$placeholder-opacity-max
:
.5
;
$placeholder-opacity-min
:
.2
;


## Stacks · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/helpers/stacks/
- fetched_at: 2026-04-29T13:45:59.918734+00:00

Added in v5.1
View on GitHub
Stacks
Shorthand helpers that build on top of our flexbox utilities to make component layout faster and easier than ever.
On this page
Stacks offer a shortcut for applying a number of flexbox properties to quickly and easily create layouts in Bootstrap. All credit for the concept and implementation goes to the open source
Pylon project
.
Heads up!
Support for gap utilities with flexbox isn’t available in Safari prior to 14.5, so consider verifying your intended browser support. Grid layout should have no issues.
Read more
.
Vertical
Use
.vstack
to create vertical layouts. Stacked items are full-width by default. Use
.gap-*
utilities to add space between items.
First item
Second item
Third item
html
<
div
class
=
"
vstack gap-3
"
>
<
div
class
=
"
p-2
"
>
First item
</
div
>
<
div
class
=
"
p-2
"
>
Second item
</
div
>
<
div
class
=
"
p-2
"
>
Third item
</
div
>
</
div
>
Horizontal
Use
.hstack
for horizontal layouts. Stacked items are vertically centered by default and only take up their necessary width. Use
.gap-*
utilities to add space between items.
First item
Second item
Third item
html
<
div
class
=
"
hstack gap-3
"
>
<
div
class
=
"
p-2
"
>
First item
</
div
>
<
div
class
=
"
p-2
"
>
Second item
</
div
>
<
div
class
=
"
p-2
"
>
Third item
</
div
>
</
div
>
Using horizontal margin utilities like
.ms-auto
as spacers:
First item
Second item
Third item
html
<
div
class
=
"
hstack gap-3
"
>
<
div
class
=
"
p-2
"
>
First item
</
div
>
<
div
class
=
"
p-2 ms-auto
"
>
Second item
</
div
>
<
div
class
=
"
p-2
"
>
Third item
</
div
>
</
div
>
And with
vertical rules
:
First item
Second item
Third item
html
<
div
class
=
"
hstack gap-3
"
>
<
div
class
=
"
p-2
"
>
First item
</
div
>
<
div
class
=
"
p-2 ms-auto
"
>
Second item
</
div
>
<
div
class
=
"
vr
"
>
</
div
>
<
div
class
=
"
p-2
"
>
Third item
</
div
>
</
div
>
Examples
Use
.vstack
to stack buttons and other elements:
html
<
div
class
=
"
vstack gap-2 col-md-5 mx-auto
"
>
<
button
type
=
"
button
"
class
=
"
btn btn-secondary
"
>
Save changes
</
button
>
<
button
type
=
"
button
"
class
=
"
btn btn-outline-secondary
"
>
Cancel
</
button
>
</
div
>
Create an inline form with
.hstack
:
html
<
div
class
=
"
hstack gap-3
"
>
<
input
class
=
"
form-control me-auto
"
type
=
"
text
"
placeholder
=
"
Add your item here...
"
aria-label
=
"
Add your item here...
"
>
<
button
type
=
"
button
"
class
=
"
btn btn-secondary
"
>
Submit
</
button
>
<
div
class
=
"
vr
"
>
</
div
>
<
button
type
=
"
button
"
class
=
"
btn btn-outline-danger
"
>
Reset
</
button
>
</
div
>
CSS
scss/helpers/_stacks.scss
.hstack
{
display
:
flex
;
flex-direction
:
row
;
align-items
:
center
;
align-self
:
stretch
;
}
.vstack
{
display
:
flex
;
flex
:
1 1 auto
;
flex-direction
:
column
;
align-self
:
stretch
;
}


## Vertical rule · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/helpers/vertical-rule/
- fetched_at: 2026-04-29T13:46:00.260245+00:00

Added in v5.1
View on GitHub
Vertical rule
Use the custom vertical rule helper to create vertical dividers like the
<hr>
element.
On this page
How it works
Vertical rules are inspired by the
<hr>
element, allowing you to create vertical dividers in common layouts. They’re styled just like
<hr>
elements:
They’re
1px
wide
They have
min-height
of
1em
Their color is set via
currentColor
and
opacity
Customize them with additional styles as needed.
Example
html
<
div
class
=
"
vr
"
>
</
div
>
Vertical rules scale their height in flex layouts:
html
<
div
class
=
"
d-flex
"
style
=
"
height
:
200px
;
"
>
<
div
class
=
"
vr
"
>
</
div
>
</
div
>
With stacks
They can also be used in
stacks
:
First item
Second item
Third item
html
<
div
class
=
"
hstack gap-3
"
>
<
div
class
=
"
p-2
"
>
First item
</
div
>
<
div
class
=
"
p-2 ms-auto
"
>
Second item
</
div
>
<
div
class
=
"
vr
"
>
</
div
>
<
div
class
=
"
p-2
"
>
Third item
</
div
>
</
div
>
CSS
Sass variables
Customize the vertical rule Sass variable to change its width.
scss/_variables.scss
$vr-border-width
:
var
(
--
#{$prefix}
border-width
)
;


## CSS variables · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/customize/css-variables/
- fetched_at: 2026-04-29T13:46:00.626757+00:00

View on GitHub
CSS variables
Use Bootstrap’s CSS custom properties for fast and forward-looking design and development.
On this page
Bootstrap includes many
CSS custom properties (variables)
in its compiled CSS for real-time customization without the need to recompile Sass. These provide easy access to commonly used values like our theme colors, breakpoints, and primary font stacks when working in your browser’s inspector, a code sandbox, or general prototyping.
All our custom properties are prefixed with
bs-
to avoid conflicts with third party CSS.
Root variables
Here are the variables we include (note that the
:root
is required) that can be accessed anywhere Bootstrap’s CSS is loaded. They’re located in our
_root.scss
file and included in our compiled dist files.
Default
These CSS variables are available everywhere, regardless of color mode.
:root,
[data-bs-theme=light]
{
--bs-blue
:
#0d6efd
;
--bs-indigo
:
#6610f2
;
--bs-purple
:
#6f42c1
;
--bs-pink
:
#d63384
;
--bs-red
:
#dc3545
;
--bs-orange
:
#fd7e14
;
--bs-yellow
:
#ffc107
;
--bs-green
:
#198754
;
--bs-teal
:
#20c997
;
--bs-cyan
:
#0dcaf0
;
--bs-black
:
#000
;
--bs-white
:
#fff
;
--bs-gray
:
#6c757d
;
--bs-gray-dark
:
#343a40
;
--bs-gray-100
:
#f8f9fa
;
--bs-gray-200
:
#e9ecef
;
--bs-gray-300
:
#dee2e6
;
--bs-gray-400
:
#ced4da
;
--bs-gray-500
:
#adb5bd
;
--bs-gray-600
:
#6c757d
;
--bs-gray-700
:
#495057
;
--bs-gray-800
:
#343a40
;
--bs-gray-900
:
#212529
;
--bs-primary
:
#0d6efd
;
--bs-secondary
:
#6c757d
;
--bs-success
:
#198754
;
--bs-info
:
#0dcaf0
;
--bs-warning
:
#ffc107
;
--bs-danger
:
#dc3545
;
--bs-light
:
#f8f9fa
;
--bs-dark
:
#212529
;
--bs-primary-rgb
:
13
,
110
,
253
;
--bs-secondary-rgb
:
108
,
117
,
125
;
--bs-success-rgb
:
25
,
135
,
84
;
--bs-info-rgb
:
13
,
202
,
240
;
--bs-warning-rgb
:
255
,
193
,
7
;
--bs-danger-rgb
:
220
,
53
,
69
;
--bs-light-rgb
:
248
,
249
,
250
;
--bs-dark-rgb
:
33
,
37
,
41
;
--bs-primary-text-emphasis
:
#052c65
;
--bs-secondary-text-emphasis
:
#2b2f32
;
--bs-success-text-emphasis
:
#0a3622
;
--bs-info-text-emphasis
:
#055160
;
--bs-warning-text-emphasis
:
#664d03
;
--bs-danger-text-emphasis
:
#58151c
;
--bs-light-text-emphasis
:
#495057
;
--bs-dark-text-emphasis
:
#495057
;
--bs-primary-bg-subtle
:
#cfe2ff
;
--bs-secondary-bg-subtle
:
#e2e3e5
;
--bs-success-bg-subtle
:
#d1e7dd
;
--bs-info-bg-subtle
:
#cff4fc
;
--bs-warning-bg-subtle
:
#fff3cd
;
--bs-danger-bg-subtle
:
#f8d7da
;
--bs-light-bg-subtle
:
#fcfcfd
;
--bs-dark-bg-subtle
:
#ced4da
;
--bs-primary-border-subtle
:
#9ec5fe
;
--bs-secondary-border-subtle
:
#c4c8cb
;
--bs-success-border-subtle
:
#a3cfbb
;
--bs-info-border-subtle
:
#9eeaf9
;
--bs-warning-border-subtle
:
#ffe69c
;
--bs-danger-border-subtle
:
#f1aeb5
;
--bs-light-border-subtle
:
#e9ecef
;
--bs-dark-border-subtle
:
#adb5bd
;
--bs-white-rgb
:
255
,
255
,
255
;
--bs-black-rgb
:
0
,
0
,
0
;
--bs-font-sans-serif
:
system-ui
,
-apple-system
,
"Segoe UI"
,
Roboto
,
"Helvetica Neue"
,
"Noto Sans"
,
"Liberation Sans"
,
Arial
,
sans-serif
,
"Apple Color Emoji"
,
"Segoe UI Emoji"
,
"Segoe UI Symbol"
,
"Noto Color Emoji"
;
--bs-font-monospace
:
SFMono-Regular
,
Menlo
,
Monaco
,
Consolas
,
"Liberation Mono"
,
"Courier New"
,
monospace
;
--bs-gradient
:
linear-gradient
(
180deg
,
rgba
(
255
,
255
,
255
,
0.15
)
,
rgba
(
255
,
255
,
255
,
0
)
)
;
--bs-body-font-family
:
var
(
--bs-font-sans-serif
)
;
--bs-body-font-size
:
1rem
;
--bs-body-font-weight
:
400
;
--bs-body-line-height
:
1.5
;
--bs-body-color
:
#212529
;
--bs-body-color-rgb
:
33
,
37
,
41
;
--bs-body-bg
:
#fff
;
--bs-body-bg-rgb
:
255
,
255
,
255
;
--bs-emphasis-color
:
#000
;
--bs-emphasis-color-rgb
:
0
,
0
,
0
;
--bs-secondary-color
:
rgba
(
33
,
37
,
41
,
0.75
)
;
--bs-secondary-color-rgb
:
33
,
37
,
41
;
--bs-secondary-bg
:
#e9ecef
;
--bs-secondary-bg-rgb
:
233
,
236
,
239
;
--bs-tertiary-color
:
rgba
(
33
,
37
,
41
,
0.5
)
;
--bs-tertiary-color-rgb
:
33
,
37
,
41
;
--bs-tertiary-bg
:
#f8f9fa
;
--bs-tertiary-bg-rgb
:
248
,
249
,
250
;
--bs-heading-color
:
inherit
;
--bs-link-color
:
#0d6efd
;
--bs-link-color-rgb
:
13
,
110
,
253
;
--bs-link-decoration
:
underline
;
--bs-link-hover-color
:
#0a58ca
;
--bs-link-hover-color-rgb
:
10
,
88
,
202
;
--bs-code-color
:
#d63384
;
--bs-highlight-color
:
#212529
;
--bs-highlight-bg
:
#fff3cd
;
--bs-border-width
:
1px
;
--bs-border-style
:
solid
;
--bs-border-color
:
#dee2e6
;
--bs-border-color-translucent
:
rgba
(
0
,
0
,
0
,
0.175
)
;
--bs-border-radius
:
0.375rem
;
--bs-border-radius-sm
:
0.25rem
;
--bs-border-radius-lg
:
0.5rem
;
--bs-border-radius-xl
:
1rem
;
--bs-border-radius-xxl
:
2rem
;
--bs-border-radius-2xl
:
var
(
--bs-border-radius-xxl
)
;
--bs-border-radius-pill
:
50rem
;
--bs-box-shadow
:
0 0.5rem 1rem
rgba
(
0
,
0
,
0
,
0.15
)
;
--bs-box-shadow-sm
:
0 0.125rem 0.25rem
rgba
(
0
,
0
,
0
,
0.075
)
;
--bs-box-shadow-lg
:
0 1rem 3rem
rgba
(
0
,
0
,
0
,
0.175
)
;
--bs-box-shadow-inset
:
inset 0 1px 2px
rgba
(
0
,
0
,
0
,
0.075
)
;
--bs-focus-ring-width
:
0.25rem
;
--bs-focus-ring-opacity
:
0.25
;
--bs-focus-ring-color
:
rgba
(
13
,
110
,
253
,
0.25
)
;
--bs-form-valid-color
:
#198754
;
--bs-form-valid-border-color
:
#198754
;
--bs-form-invalid-color
:
#dc3545
;
--bs-form-invalid-border-color
:
#dc3545
;
}
Dark mode
These variables are scoped to our built-in dark mode.
[data-bs-theme=dark]
{
color-scheme
:
dark
;
--bs-body-color
:
#dee2e6
;
--bs-body-color-rgb
:
222
,
226
,
230
;
--bs-body-bg
:
#212529
;
--bs-body-bg-rgb
:
33
,
37
,
41
;
--bs-emphasis-color
:
#fff
;
--bs-emphasis-color-rgb
:
255
,
255
,
255
;
--bs-secondary-color
:
rgba
(
222
,
226
,
230
,
0.75
)
;
--bs-secondary-color-rgb
:
222
,
226
,
230
;
--bs-secondary-bg
:
#343a40
;
--bs-secondary-bg-rgb
:
52
,
58
,
64
;
--bs-tertiary-color
:
rgba
(
222
,
226
,
230
,
0.5
)
;
--bs-tertiary-color-rgb
:
222
,
226
,
230
;
--bs-tertiary-bg
:
#2b3035
;
--bs-tertiary-bg-rgb
:
43
,
48
,
53
;
--bs-primary-text-emphasis
:
#6ea8fe
;
--bs-secondary-text-emphasis
:
#a7acb1
;
--bs-success-text-emphasis
:
#75b798
;
--bs-info-text-emphasis
:
#6edff6
;
--bs-warning-text-emphasis
:
#ffda6a
;
--bs-danger-text-emphasis
:
#ea868f
;
--bs-light-text-emphasis
:
#f8f9fa
;
--bs-dark-text-emphasis
:
#dee2e6
;
--bs-primary-bg-subtle
:
#031633
;
--bs-secondary-bg-subtle
:
#161719
;
--bs-success-bg-subtle
:
#051b11
;
--bs-info-bg-subtle
:
#032830
;
--bs-warning-bg-subtle
:
#332701
;
--bs-danger-bg-subtle
:
#2c0b0e
;
--bs-light-bg-subtle
:
#343a40
;
--bs-dark-bg-subtle
:
#1a1d20
;
--bs-primary-border-subtle
:
#084298
;
--bs-secondary-border-subtle
:
#41464b
;
--bs-success-border-subtle
:
#0f5132
;
--bs-info-border-subtle
:
#087990
;
--bs-warning-border-subtle
:
#997404
;
--bs-danger-border-subtle
:
#842029
;
--bs-light-border-subtle
:
#495057
;
--bs-dark-border-subtle
:
#343a40
;
--bs-heading-color
:
inherit
;
--bs-link-color
:
#6ea8fe
;
--bs-link-hover-color
:
#8bb9fe
;
--bs-link-color-rgb
:
110
,
168
,
254
;
--bs-link-hover-color-rgb
:
139
,
185
,
254
;
--bs-code-color
:
#e685b5
;
--bs-highlight-color
:
#dee2e6
;
--bs-highlight-bg
:
#664d03
;
--bs-border-color
:
#495057
;
--bs-border-color-translucent
:
rgba
(
255
,
255
,
255
,
0.15
)
;
--bs-form-valid-color
:
#75b798
;
--bs-form-valid-border-color
:
#75b798
;
--bs-form-invalid-color
:
#ea868f
;
--bs-form-invalid-border-color
:
#ea868f
;
}
Component variables
Bootstrap 5 is increasingly making use of custom properties as local variables for various components. This way we reduce our compiled CSS, ensure styles aren’t inherited in places like nested tables, and allow some basic restyling and extending of Bootstrap components after Sass compilation.
Have a look at our table documentation for some
insight into how we’re using CSS variables
. Our
navbars also use CSS variables
as of v5.2.0. We’re also using CSS variables across our grids—primarily for gutters the
new opt-in CSS grid
—with more component usage coming in the future.
Whenever possible, we'll assign CSS variables at the base component level (e.g.,
.navbar
for navbar and its sub-components). This reduces guessing on where and how to customize, and allows for easy modifications by our team in future updates.
Prefix
Most CSS variables use a prefix to avoid collisions with your own codebase. This prefix is in addition to the
--
that’s required on every CSS variable.
Customize the prefix via the
$prefix
Sass variable. By default, it’s set to
bs-
(note the trailing dash).
Examples
CSS variables offer similar flexibility to Sass’s variables, but without the need for compilation before being served to the browser. For example, here we’re resetting our page’s font and link styles with CSS variables.
body
{
font
:
1rem/1.5
var
(
--bs-font-sans-serif
)
;
}
a
{
color
:
var
(
--bs-blue
)
;
}
Focus variables
Added in v5.3.0
Bootstrap provides custom
:focus
styles using a combination of Sass and CSS variables that can be optionally added to specific components and elements. We do not yet globally override all
:focus
styles.
In our Sass, we set default values that can be customized before compiling.
scss/_variables.scss
$focus-ring-width
:
.25rem
;
$focus-ring-opacity
:
.25
;
$focus-ring-color
:
rgba
(
$primary
,
$focus-ring-opacity
)
;
$focus-ring-blur
:
0
;
$focus-ring-box-shadow
:
0 0
$focus-ring-blur
$focus-ring-width
$focus-ring-color
;
Those variables are then reassigned to
:root
level CSS variables that can be customized in real-time, including with options for
x
and
y
offsets (which default to their fallback value of
0
).
scss/_root.scss
--
#{$prefix}
focus-ring-width
:
#{$focus-ring-width}
;
--
#{$prefix}
focus-ring-opacity
:
#{$focus-ring-opacity}
;
--
#{$prefix}
focus-ring-color
:
#{$focus-ring-color}
;
Grid breakpoints
While we include our grid breakpoints as CSS variables (except for
xs
), be aware that
CSS variables do not work in media queries
. This is by design in the CSS spec for variables, but may change in coming years with support for
env()
variables. Check out
this Stack Overflow answer
for some helpful links. In the meantime, you can use these variables in other CSS situations, as well as in your JavaScript.


## Customize · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/customize/overview/
- fetched_at: 2026-04-29T13:46:00.955510+00:00

View on GitHub
Customize
Learn how to theme, customize, and extend Bootstrap with Sass, a boatload of global options, an expansive color system, and more.
Sass
Utilize our source Sass files to take advantage of variables, maps, mixins, and functions.
Options
Customize Bootstrap with built-in variables to easily toggle global CSS preferences.
Color
Learn about and customize the color systems that support the entire toolkit.
Color modes
Explore our default light mode and the new dark mode, or create custom color modes yourself.
Components
Learn how we build nearly all our components responsively and with base and modifier classes.
CSS variables
Use Bootstrap’s CSS custom properties for fast and forward-looking design and development.
Optimize
Keep your projects lean, responsive, and maintainable so you can deliver the best experience.
Overview
There are multiple ways to customize Bootstrap. Your best path can depend on your project, the complexity of your build tools, the version of Bootstrap you’re using, browser support, and more.
Our two preferred methods are:
Using Bootstrap
via package manager
so you can use and extend our source files.
Using Bootstrap’s compiled distribution files or
jsDelivr
so you can add onto or override Bootstrap’s styles.
While we cannot go into details here on how to use every package manager, we can give some guidance on
using Bootstrap with your own Sass compiler
.
For those who want to use the distribution files, review the
getting started page
for how to include those files and an example HTML page. From there, consult the docs for the layout, components, and behaviors you’d like to use.
As you familiarize yourself with Bootstrap, continue exploring this section for more details on how to utilize our global options, making use of and changing our color system, how we build our components, how to use our growing list of CSS custom properties, and how to optimize your code when building with Bootstrap.
CSPs and embedded SVGs
Several Bootstrap components include embedded SVGs in our CSS to style components consistently and easily across browsers and devices.
For organizations with more strict
CSP
configurations
, we’ve documented all instances of our embedded SVGs (all of which are applied via
background-image
) so you can more thoroughly review your options.
Accordion
Carousel controls
Close button
(used in alerts and modals)
Form checkboxes and radio buttons
Form switches
Form validation icons
Navbar toggle buttons
Select menus
Based on
community conversation
, some options for addressing this in your own codebase include
replacing the URLs with locally hosted assets
, removing the images and using inline images (not possible in all components), and modifying your CSP. Our recommendation is to carefully review your own security policies and decide on the best path forward, if necessary.


## Forms · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/forms/overview/
- fetched_at: 2026-04-29T13:46:01.197136+00:00

View on GitHub
Forms
Examples and usage guidelines for form control styles, layout options, and custom components for creating a wide variety of forms.
On this page
Form control
Style textual inputs and textareas with support for multiple states.
Select
Improve browser default select elements with a custom initial appearance.
Checks & radios
Use our custom radio buttons and checkboxes in forms for selecting input options.
Range
Replace browser default range inputs with our custom version.
Input group
Attach labels and buttons to your inputs for increased semantic value.
Floating labels
Create beautifully simple form labels that float over your input fields.
Layout
Create inline, horizontal, or complex grid-based layouts with your forms.
Validation
Validate your forms with custom or native validation behaviors and styles.
Overview
Bootstrap’s form controls expand on
our Rebooted form styles
with classes. Use these classes to opt into their customized displays for a more consistent rendering across browsers and devices.
Be sure to use an appropriate
type
attribute on all inputs (e.g.,
email
for email address or
number
for numerical information) to take advantage of newer input controls like email verification, number selection, and more.
Here’s a quick example to demonstrate Bootstrap’s form styles. Keep reading for documentation on required classes, form layout, and more.
html
<
form
>
<
div
class
=
"
mb-3
"
>
<
label
for
=
"
exampleInputEmail1
"
class
=
"
form-label
"
>
Email address
</
label
>
<
input
type
=
"
email
"
class
=
"
form-control
"
id
=
"
exampleInputEmail1
"
aria-describedby
=
"
emailHelp
"
>
<
div
id
=
"
emailHelp
"
class
=
"
form-text
"
>
We'll never share your email with anyone else.
</
div
>
</
div
>
<
div
class
=
"
mb-3
"
>
<
label
for
=
"
exampleInputPassword1
"
class
=
"
form-label
"
>
Password
</
label
>
<
input
type
=
"
password
"
class
=
"
form-control
"
id
=
"
exampleInputPassword1
"
>
</
div
>
<
div
class
=
"
mb-3 form-check
"
>
<
input
type
=
"
checkbox
"
class
=
"
form-check-input
"
id
=
"
exampleCheck1
"
>
<
label
class
=
"
form-check-label
"
for
=
"
exampleCheck1
"
>
Check me out
</
label
>
</
div
>
<
button
type
=
"
submit
"
class
=
"
btn btn-primary
"
>
Submit
</
button
>
</
form
>
Disabled forms
Add the
disabled
boolean attribute on an input to prevent user interactions and make it appear lighter.
<
input
class
=
"
form-control
"
id
=
"
disabledInput
"
type
=
"
text
"
placeholder
=
"
Disabled input here...
"
disabled
>
Add the
disabled
attribute to a
<fieldset>
to disable all the controls within. Browsers treat all native form controls (
<input>
,
<select>
, and
<button>
elements) inside a
<fieldset disabled>
as disabled, preventing both keyboard and mouse interactions on them.
However, if your form also includes custom button-like elements such as
<a class="btn btn-*">...</a>
, these will only be given a style of
pointer-events: none
, meaning they are still focusable and operable using the keyboard. In this case, you must manually modify these controls by adding
tabindex="-1"
to prevent them from receiving focus and
aria-disabled="disabled"
to signal their state to assistive technologies.
html
<
form
>
<
fieldset
disabled
>
<
legend
>
Disabled fieldset example
</
legend
>
<
div
class
=
"
mb-3
"
>
<
label
for
=
"
disabledTextInput
"
class
=
"
form-label
"
>
Disabled input
</
label
>
<
input
type
=
"
text
"
id
=
"
disabledTextInput
"
class
=
"
form-control
"
placeholder
=
"
Disabled input
"
>
</
div
>
<
div
class
=
"
mb-3
"
>
<
label
for
=
"
disabledSelect
"
class
=
"
form-label
"
>
Disabled select menu
</
label
>
<
select
id
=
"
disabledSelect
"
class
=
"
form-select
"
>
<
option
>
Disabled select
</
option
>
</
select
>
</
div
>
<
div
class
=
"
mb-3
"
>
<
div
class
=
"
form-check
"
>
<
input
class
=
"
form-check-input
"
type
=
"
checkbox
"
id
=
"
disabledFieldsetCheck
"
disabled
>
<
label
class
=
"
form-check-label
"
for
=
"
disabledFieldsetCheck
"
>
Can’t check this
</
label
>
</
div
>
</
div
>
<
button
type
=
"
submit
"
class
=
"
btn btn-primary
"
>
Submit
</
button
>
</
fieldset
>
</
form
>
Accessibility
Ensure that all form controls have an appropriate accessible name so that their purpose can be conveyed to users of assistive technologies. The simplest way to achieve this is to use a
<label>
element, or—in the case of buttons—to include sufficiently descriptive text as part of the
<button>...</button>
content.
For situations where it’s not possible to include a visible
<label>
or appropriate text content, there are alternative ways of still providing an accessible name, such as:
<label>
elements hidden using the
.visually-hidden
class
Pointing to an existing element that can act as a label using
aria-labelledby
Providing a
title
attribute
Explicitly setting the accessible name on an element using
aria-label
If none of these are present, assistive technologies may resort to using the
placeholder
attribute as a fallback for the accessible name on
<input>
and
<textarea>
elements. The examples in this section provide a few suggested, case-specific approaches.
While using visually hidden content (
.visually-hidden
,
aria-label
, and even
placeholder
content, which disappears once a form field has content) will benefit assistive technology users, a lack of visible label text may still be problematic for certain users. Some form of visible label is generally the best approach, both for accessibility and usability.
CSS
Many form variables are set at a general level to be re-used and extended by individual form components. You’ll see these most often as
$input-btn-*
and
$input-*
variables.
Sass variables
$input-btn-*
variables are shared global variables between our
buttons
and our form components. You’ll find these frequently reassigned as values to other component-specific variables.
scss/_variables.scss
$input-btn-padding-y
:
.375rem
;
$input-btn-padding-x
:
.75rem
;
$input-btn-font-family
:
null
;
$input-btn-font-size
:
$font-size-base
;
$input-btn-line-height
:
$line-height-base
;
$input-btn-focus-width
:
$focus-ring-width
;
$input-btn-focus-color-opacity
:
$focus-ring-opacity
;
$input-btn-focus-color
:
$focus-ring-color
;
$input-btn-focus-blur
:
$focus-ring-blur
;
$input-btn-focus-box-shadow
:
$focus-ring-box-shadow
;
$input-btn-padding-y-sm
:
.25rem
;
$input-btn-padding-x-sm
:
.5rem
;
$input-btn-font-size-sm
:
$font-size-sm
;
$input-btn-padding-y-lg
:
.5rem
;
$input-btn-padding-x-lg
:
1rem
;
$input-btn-font-size-lg
:
$font-size-lg
;
$input-btn-border-width
:
var
(
--
#{$prefix}
border-width
)
;


## Sass · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/customize/sass/
- fetched_at: 2026-04-29T13:46:01.570645+00:00

View on GitHub
Sass
Utilize our source Sass files to take advantage of variables, maps, mixins, and functions to help you build faster and customize your project.
On this page
Utilize our source Sass files to take advantage of variables, maps, mixins, and more.
Sass deprecation warnings are shown when compiling source Sass files with the latest versions of Dart Sass. This does not prevent compilation or usage of Bootstrap. We’re
working on a long-term fix
, but in the meantime these deprecation notices can be ignored.
File structure
Whenever possible, avoid modifying Bootstrap’s core files. For Sass, that means creating your own stylesheet that imports Bootstrap so you can modify and extend it. Assuming you’re using a package manager like npm, you’ll have a file structure that looks like this:
your-project/
├── scss/
│ └── custom.scss
└── node_modules/
│ └── bootstrap/
│ ├── js/
│ └── scss/
└── index.html
If you’ve downloaded our source files and aren’t using a package manager, you’ll want to manually create something similar to that structure, keeping Bootstrap’s source files separate from your own.
your-project/
├── scss/
│ └── custom.scss
├── bootstrap/
│ ├── js/
│ └── scss/
└── index.html
Importing
In your
custom.scss
, you’ll import Bootstrap’s source Sass files. You have two options: include all of Bootstrap, or pick the parts you need. We encourage the latter, though be aware there are some requirements and dependencies across our components. You also will need to include some JavaScript for our plugins.
// Custom.scss
// Option A: Include all of Bootstrap
// Include any default variable overrides here (though functions won’t be available)
@import
"../node_modules/bootstrap/scss/bootstrap"
;
// Then add additional custom code here
// Custom.scss
// Option B: Include parts of Bootstrap
// 1. Include functions first (so you can manipulate colors, SVGs, calc, etc)
@import
"../node_modules/bootstrap/scss/functions"
;
// 2. Include any default variable overrides here
// 3. Include remainder of required Bootstrap stylesheets (including any separate color mode stylesheets)
@import
"../node_modules/bootstrap/scss/variables"
;
@import
"../node_modules/bootstrap/scss/variables-dark"
;
// 4. Include any default map overrides here
// 5. Include remainder of required parts
@import
"../node_modules/bootstrap/scss/maps"
;
@import
"../node_modules/bootstrap/scss/mixins"
;
@import
"../node_modules/bootstrap/scss/root"
;
// 6. Include any other optional stylesheet partials as desired; list below is not inclusive of all available stylesheets
@import
"../node_modules/bootstrap/scss/utilities"
;
@import
"../node_modules/bootstrap/scss/reboot"
;
@import
"../node_modules/bootstrap/scss/type"
;
@import
"../node_modules/bootstrap/scss/images"
;
@import
"../node_modules/bootstrap/scss/containers"
;
@import
"../node_modules/bootstrap/scss/grid"
;
@import
"../node_modules/bootstrap/scss/helpers"
;
// ...
// 7. Optionally include utilities API last to generate classes based on the Sass map in `_utilities.scss`
@import
"../node_modules/bootstrap/scss/utilities/api"
;
// 8. Add additional custom code here
With that setup in place, you can begin to modify any of the Sass variables and maps in your
custom.scss
. You can also start to add parts of Bootstrap under the
// Optional
section as needed. We suggest using the full import stack from our
bootstrap.scss
file as your starting point.
Compiling
In order to use your custom Sass code as CSS in the browser, you need a Sass compiler. Sass ships as a CLI package, but you can also compile it with other build tools like
Gulp
or
Webpack
, or with GUI applications. Some IDEs also have Sass compilers built in or as downloadable extensions.
We like to use the CLI to compile our Sass, but you can use whichever method you prefer. From the command line, run the following:
# Install Sass globally
npm
install
-g
sass
# Watch your custom Sass for changes and compile it to CSS
sass
--watch
./scss/custom.scss ./css/custom.css
Learn more about your options at
sass-lang.com/install
and
compiling with VS Code
.
Using Bootstrap with another build tool?
Consider reading our guides for compiling with
Webpack
,
Parcel
, or
Vite
. We also have production-ready demos in
our examples repository on GitHub
.
Including
Once your CSS is compiled, you can include it in your HTML files. Inside your
index.html
you’ll want to include your compiled CSS file. Be sure to update the path to your compiled CSS file if you’ve changed it.
<!
doctype
html
>
<
html
lang
=
"
en
"
>
<
head
>
<
meta
charset
=
"
utf-8
"
>
<
meta
name
=
"
viewport
"
content
=
"
width=device-width, initial-scale=1
"
>
<
title
>
Custom Bootstrap
</
title
>
<
link
href
=
"
/css/custom.css
"
rel
=
"
stylesheet
"
>
</
head
>
<
body
>
<
h1
>
Hello, world!
</
h1
>
</
body
>
</
html
>
Variable defaults
Every Sass variable in Bootstrap includes the
!default
flag allowing you to override the variable’s default value in your own Sass without modifying Bootstrap’s source code. Copy and paste variables as needed, modify their values, and remove the
!default
flag. If a variable has already been assigned, then it won’t be re-assigned by the default values in Bootstrap.
You will find the complete list of Bootstrap’s variables in
scss/_variables.scss
. Some variables are set to
null
, these variables don’t output the property unless they are overridden in your configuration.
Variable overrides must come after our functions are imported, but before the rest of the imports.
Here’s an example that changes the
background-color
and
color
for the
<body>
when importing and compiling Bootstrap via npm:
// Required
@import
"../node_modules/bootstrap/scss/functions"
;
// Default variable overrides
$body-bg
:
#000
;
$body-color
:
#111
;
// Required
@import
"../node_modules/bootstrap/scss/variables"
;
@import
"../node_modules/bootstrap/scss/variables-dark"
;
@import
"../node_modules/bootstrap/scss/maps"
;
@import
"../node_modules/bootstrap/scss/mixins"
;
@import
"../node_modules/bootstrap/scss/root"
;
// Optional Bootstrap components here
@import
"../node_modules/bootstrap/scss/reboot"
;
@import
"../node_modules/bootstrap/scss/type"
;
// etc
Repeat as necessary for any variable in Bootstrap, including the global options below.
Get started with Bootstrap via npm with our starter project!
Head to the
Sass & JS example
template repository to see how to build and customize Bootstrap in your own npm project. Includes Sass compiler, Autoprefixer, Stylelint, PurgeCSS, and Bootstrap Icons.
Maps and loops
Bootstrap includes a handful of Sass maps, key value pairs that make it easier to generate families of related CSS. We use Sass maps for our colors, grid breakpoints, and more. Just like Sass variables, all Sass maps include the
!default
flag and can be overridden and extended.
Some of our Sass maps are merged into empty ones by default. This is done to allow easy expansion of a given Sass map, but comes at the cost of making
removing
items from a map slightly more difficult.
Modify map
All variables in the
$theme-colors
map are defined as standalone variables. To modify an existing color in our
$theme-colors
map, add the following to your custom Sass file:
$primary
:
#0074d9
;
$danger
:
#ff4136
;
Later on, these variables are set in Bootstrap’s
$theme-colors
map:
$theme-colors
:
(
"primary"
:
$primary
,
"danger"
:
$danger
)
;
Add to map
Add new colors to
$theme-colors
, or any other map, by creating a new Sass map with your custom values and merging it with the original map. In this case, we'll create a new
$custom-colors
map and merge it with
$theme-colors
.
// Create your own map
$custom-colors
:
(
"custom-color"
:
#900
)
;
// Merge the maps
$theme-colors
:
map-merge
(
$theme-colors
,
$custom-colors
)
;
Remove from map
To remove colors from
$theme-colors
, or any other map, use
map-remove
. Be aware you must insert
$theme-colors
between our requirements just after its definition in
variables
and before its usage in
maps
:
// Required
@import
"../node_modules/bootstrap/scss/functions"
;
@import
"../node_modules/bootstrap/scss/variables"
;
@import
"../node_modules/bootstrap/scss/variables-dark"
;
$theme-colors
:
map-remove
(
$theme-colors
,
"info"
,
"light"
,
"dark"
)
;
@import
"../node_modules/bootstrap/scss/maps"
;
@import
"../node_modules/bootstrap/scss/mixins"
;
@import
"../node_modules/bootstrap/scss/root"
;
// Optional
@import
"../node_modules/bootstrap/scss/reboot"
;
@import
"../node_modules/bootstrap/scss/type"
;
// etc
Required keys
Bootstrap assumes the presence of some specific keys within Sass maps as we used and extend these ourselves. As you customize the included maps, you may encounter errors where a specific Sass map’s key is being used.
For example, we use the
primary
,
success
, and
danger
keys from
$theme-colors
for links, buttons, and form states. Replacing the values of these keys should present no issues, but removing them may cause Sass compilation issues. In these instances, you’ll need to modify the Sass code that makes use of those values.
Functions
Colors
Next to the
Sass maps
we have, theme colors can also be used as standalone variables, like
$primary
.
.custom-element
{
color
:
$gray-100
;
background-color
:
$dark
;
}
You can lighten or darken colors with Bootstrap’s
tint-color()
and
shade-color()
functions. These functions will mix colors with black or white, unlike Sass’ native
lighten()
and
darken()
functions which will change the lightness by a fixed amount, which often doesn’t lead to the desired effect.
shift-color()
combines these two functions by shading the color if the weight is positive and tinting the color if the weight is negative.
scss/_functions.scss
// Tint a color: mix a color with white
@function
tint-color
(
$color
,
$weight
)
{
@return
mix
(
white
,
$color
,
$weight
)
;
}
// Shade a color: mix a color with black
@function
shade-color
(
$color
,
$weight
)
{
@return
mix
(
black
,
$color
,
$weight
)
;
}
// Shade the color if the weight is positive, else tint it
@function
shift-color
(
$color
,
$weight
)
{
@return
if
(
$weight
>
0
,
shade-color
(
$color
,
$weight
)
,
tint-color
(
$color
,
-
$weight
)
)
;
}
In practice, you’d call the function and pass in the color and weight parameters.
.custom-element
{
color
:
tint-color
(
$primary
,
10%
)
;
}
.custom-element-2
{
color
:
shade-color
(
$danger
,
30%
)
;
}
.custom-element-3
{
color
:
shift-color
(
$success
,
40%
)
;
background-color
:
shift-color
(
$success
,
-60%
)
;
}
Color contrast
In order to meet the
Web Content Accessibility Guidelines (WCAG)
contrast requirements, authors
must
provide a minimum
text color contrast of 4.5:1
and a minimum
non-text color contrast of 3:1
, with very few exceptions.
To help with this, we included the
color-contrast
function in Bootstrap. It uses the
WCAG contrast ratio algorithm
for calculating contrast thresholds based on
relative luminance
in an
sRGB
color space to automatically return a light (
#fff
), dark (
#212529
) or black (
#000
) contrast color based on the specified base color. This function is especially useful for mixins or loops where you’re generating multiple classes.
For example, to generate color swatches from our
$theme-colors
map:
@each
$color
,
$value
in
$theme-colors
{
.swatch-
#{$color}
{
color
:
color-contrast
(
$value
)
;
}
}
It can also be used for one-off contrast needs:
.custom-element
{
color
:
color-contrast
(
#000
)
;
// returns `color: #fff`
}
You can also specify a base color with our color map functions:
.custom-element
{
color
:
color-contrast
(
$dark
)
;
// returns `color: #fff`
}
Escape SVG
We use the
escape-svg
function to escape the
<
,
>
and
#
characters for SVG background images. When using the
escape-svg
function, data URIs must be quoted.
Add and Subtract functions
We use the
add
and
subtract
functions to wrap the CSS
calc
function. The primary purpose of these functions is to avoid errors when a “unitless”
0
value is passed into a
calc
expression. Expressions like
calc(10px - 0)
will return an error in all browsers, despite being mathematically correct.
Example where the calc is valid:
$border-radius
:
.25rem
;
$border-width
:
1px
;
.element
{
// Output calc(.25rem - 1px) is valid
border-radius
:
calc
(
$border-radius
-
$border-width
)
;
}
.element
{
// Output the same calc(.25rem - 1px) as above
border-radius
:
subtract
(
$border-radius
,
$border-width
)
;
}
Example where the calc is invalid:
$border-radius
:
.25rem
;
$border-width
:
0
;
.element
{
// Output calc(.25rem - 0) is invalid
border-radius
:
calc
(
$border-radius
-
$border-width
)
;
}
.element
{
// Output .25rem
border-radius
:
subtract
(
$border-radius
,
$border-width
)
;
}
Mixins
Our
scss/mixins/
directory has a ton of mixins that power parts of Bootstrap and can also be used across your own project.
Color schemes
A shorthand mixin for the
prefers-color-scheme
media query is available with support for
light
and
dark
color schemes. See
the color modes documentation
for information on our color mode mixin.
scss/mixins/_color-scheme.scss
@mixin
color-scheme
(
$name
)
{
@media
(
prefers-color-scheme
:
#{$name}
)
{
@content
;
}
}
.custom-element
{
@include
color-scheme
(
light
)
{
// Insert light mode styles here
}
@include
color-scheme
(
dark
)
{
// Insert dark mode styles here
}
}


## Options · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/customize/options/
- fetched_at: 2026-04-29T13:46:01.915161+00:00

View on GitHub
Options
Quickly customize Bootstrap with built-in variables to easily toggle global CSS preferences for controlling style and behavior.
Customize Bootstrap with our built-in custom variables file and easily toggle global CSS preferences with new
$enable-*
Sass variables. Override a variable’s value and recompile with
npm run test
as needed.
You can find and customize these variables for key global options in Bootstrap’s
scss/_variables.scss
file.
Variable
Values
Description
$spacer
1rem
(default), or any value > 0
Specifies the default spacer value to programmatically generate our
spacer utilities
.
$enable-dark-mode
true
(default) or
false
Enables built-in
dark mode support
across the project and its components.
$enable-rounded
true
(default) or
false
Enables predefined
border-radius
styles on various components.
$enable-shadows
true
or
false
(default)
Enables predefined decorative
box-shadow
styles on various components. Does not affect
box-shadow
s used for focus states.
$enable-gradients
true
or
false
(default)
Enables predefined gradients via
background-image
styles on various components.
$enable-transitions
true
(default) or
false
Enables predefined
transition
s on various components.
$enable-reduced-motion
true
(default) or
false
Enables the
prefers-reduced-motion
media query
, which suppresses certain animations/transitions based on the users’ browser/operating system preferences.
$enable-grid-classes
true
(default) or
false
Enables the generation of CSS classes for the grid system (e.g.
.row
,
.col-md-1
, etc.).
$enable-cssgrid
true
or
false
(default)
Enables the experimental CSS Grid system (e.g.
.grid
,
.g-col-md-1
, etc.).
$enable-container-classes
true
(default) or
false
Enables the generation of CSS classes for layout containers. (New in v5.2.0)
$enable-caret
true
(default) or
false
Enables pseudo element caret on
.dropdown-toggle
.
$enable-button-pointers
true
(default) or
false
Add “hand” cursor to non-disabled button elements.
$enable-rfs
true
(default) or
false
Globally enables
RFS
.
$enable-validation-icons
true
(default) or
false
Enables
background-image
icons within textual inputs and some custom forms for validation states.
$enable-negative-margins
true
or
false
(default)
Enables the generation of
negative margin utilities
.
$enable-deprecation-messages
true
(default) or
false
Set to
false
to hide warnings when using any of the deprecated mixins and functions that are planned to be removed in
v6
.
$enable-important-utilities
true
(default) or
false
Enables the
!important
suffix in utility classes.
$enable-smooth-scroll
true
(default) or
false
Applies
scroll-behavior: smooth
globally, except for users asking for reduced motion through
prefers-reduced-motion
media query


## Color · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/customize/color/
- fetched_at: 2026-04-29T13:46:02.271671+00:00

View on GitHub
Color
Bootstrap is supported by an extensive color system that themes our styles and components. This enables more comprehensive customization and extension for any project.
On this page
Colors
Added in v5.3.0
Bootstrap’s color palette has continued to expand and become more nuanced in v5.3.0. We’ve added new variables for
secondary
and
tertiary
text and background colors, plus
{color}-bg-subtle
,
{color}-border-subtle
, and
{color}-text-emphasis
for our theme colors. These new colors are available through Sass and CSS variables (but not our color maps or utility classes) with the express goal of making it easier to customize across multiple colors modes like light and dark. These new variables are globally set on
:root
and are adapted for our new dark color mode while our original theme colors remain unchanged.
Colors ending in
-rgb
provide the
red, green, blue
values for use in
rgb()
and
rgba()
color modes. For example,
rgba(var(--bs-secondary-bg-rgb), .5)
.
Heads up!
There’s some potential confusion with our new secondary and tertiary colors, and our existing secondary theme color, as well as our light and dark theme colors. Expect this to be ironed out in v6.
Description
Swatch
Variables
Body —
Default foreground (color) and background, including components.
--bs-body-color
--bs-body-color-rgb
--bs-body-bg
--bs-body-bg-rgb
Secondary —
Use the
color
option for lighter text. Use the
bg
option for dividers and to indicate disabled component states.
--bs-secondary-color
--bs-secondary-color-rgb
--bs-secondary-bg
--bs-secondary-bg-rgb
Tertiary —
Use the
color
option for even lighter text. Use the
bg
option to style backgrounds for hover states, accents, and wells.
--bs-tertiary-color
--bs-tertiary-color-rgb
--bs-tertiary-bg
--bs-tertiary-bg-rgb
Emphasis —
For higher contrast text. Not applicable for backgrounds.
--bs-emphasis-color
--bs-emphasis-color-rgb
Border —
For component borders, dividers, and rules. Use
--bs-border-color-translucent
to blend with backgrounds with an
rgba()
value.
--bs-border-color
--bs-border-color-rgb
Primary —
Main theme color, used for hyperlinks, focus styles, and component and form active states.
--bs-primary
--bs-primary-rgb
--bs-primary-bg-subtle
--bs-primary-border-subtle
Text
--bs-primary-text-emphasis
Success —
Theme color used for positive or successful actions and information.
--bs-success
--bs-success-rgb
--bs-success-bg-subtle
--bs-success-border-subtle
Text
--bs-success-text-emphasis
Danger —
Theme color used for errors and dangerous actions.
--bs-danger
--bs-danger-rgb
--bs-danger-bg-subtle
--bs-danger-border-subtle
Text
--bs-danger-text-emphasis
Warning —
Theme color used for non-destructive warning messages.
--bs-warning
--bs-warning-rgb
--bs-warning-bg-subtle
--bs-warning-border-subtle
Text
--bs-warning-text-emphasis
Info —
Theme color used for neutral and informative content.
--bs-info
--bs-info-rgb
--bs-info-bg-subtle
--bs-info-border-subtle
Text
--bs-info-text-emphasis
Light —
Additional theme option for less contrasting colors.
--bs-light
--bs-light-rgb
--bs-light-bg-subtle
--bs-light-border-subtle
Text
--bs-light-text-emphasis
Dark —
Additional theme option for higher contrasting colors.
--bs-dark
--bs-dark-rgb
--bs-dark-bg-subtle
--bs-dark-border-subtle
Text
--bs-dark-text-emphasis
Using the new colors
These new colors are accessible via CSS variables and utility classes—like
--bs-primary-bg-subtle
and
.bg-primary-subtle
—allowing you to compose your own CSS rules with the variables, or to quickly apply styles via classes. The utilities are built with the color’s associated CSS variables, and since we customize those CSS variables for dark mode, they are also adaptive to color mode by default.
Example element with utilities
html
<
div
class
=
"
p-3 text-primary-emphasis bg-primary-subtle border border-primary-subtle rounded-3
"
>
Example element with utilities
</
div
>
Theme colors
We use a subset of all colors to create a smaller color palette for generating color schemes, also available as Sass variables and a Sass map in Bootstrap’s
scss/_variables.scss
file.
Primary
Secondary
Success
Danger
Warning
Info
Light
Dark
All these colors are available as a Sass map,
$theme-colors
.
scss/_variables.scss
$theme-colors
:
(
"primary"
:
$primary
,
"secondary"
:
$secondary
,
"success"
:
$success
,
"info"
:
$info
,
"warning"
:
$warning
,
"danger"
:
$danger
,
"light"
:
$light
,
"dark"
:
$dark
)
;
Check out
our Sass maps and loops docs
for how to modify these colors.
All colors
All Bootstrap colors are available as Sass variables and a Sass map in
scss/_variables.scss
file. To avoid increased file sizes, we don’t create text or background color classes for each of these variables. Instead, we choose a subset of these colors for a
theme palette
.
Be sure to monitor contrast ratios as you customize colors. As shown below, we’ve added three contrast ratios to each of the main colors—one for the swatch’s current colors, one for against white, and one for against black.
$blue
#0d6efd
$blue-100
$blue-200
$blue-300
$blue-400
$blue-500
$blue-600
$blue-700
$blue-800
$blue-900
$indigo
#6610f2
$indigo-100
$indigo-200
$indigo-300
$indigo-400
$indigo-500
$indigo-600
$indigo-700
$indigo-800
$indigo-900
$purple
#6f42c1
$purple-100
$purple-200
$purple-300
$purple-400
$purple-500
$purple-600
$purple-700
$purple-800
$purple-900
$pink
#d63384
$pink-100
$pink-200
$pink-300
$pink-400
$pink-500
$pink-600
$pink-700
$pink-800
$pink-900
$red
#dc3545
$red-100
$red-200
$red-300
$red-400
$red-500
$red-600
$red-700
$red-800
$red-900
$orange
#fd7e14
$orange-100
$orange-200
$orange-300
$orange-400
$orange-500
$orange-600
$orange-700
$orange-800
$orange-900
$yellow
#ffc107
$yellow-100
$yellow-200
$yellow-300
$yellow-400
$yellow-500
$yellow-600
$yellow-700
$yellow-800
$yellow-900
$green
#198754
$green-100
$green-200
$green-300
$green-400
$green-500
$green-600
$green-700
$green-800
$green-900
$teal
#20c997
$teal-100
$teal-200
$teal-300
$teal-400
$teal-500
$teal-600
$teal-700
$teal-800
$teal-900
$cyan
#0dcaf0
$cyan-100
$cyan-200
$cyan-300
$cyan-400
$cyan-500
$cyan-600
$cyan-700
$cyan-800
$cyan-900
$gray-500
#adb5bd
$gray-100
$gray-200
$gray-300
$gray-400
$gray-500
$gray-600
$gray-700
$gray-800
$gray-900
$black
#000
$white
#fff
Notes on Sass
Sass cannot programmatically generate variables, so we manually created variables for every tint and shade ourselves. We specify the midpoint value (e.g.,
$blue-500
) and use custom color functions to tint (lighten) or shade (darken) our colors via Sass’s
mix()
color function.
Using
mix()
is not the same as
lighten()
and
darken()
—the former blends the specified color with white or black, while the latter only adjusts the lightness value of each color. The result is a much more complete suite of colors, as
shown in this CodePen demo
.
Our
tint-color()
and
shade-color()
functions use
mix()
alongside our
$theme-color-interval
variable, which specifies a stepped percentage value for each mixed color we produce. See the
scss/_functions.scss
and
scss/_variables.scss
files for the full source code.
Color Sass maps
Bootstrap’s source Sass files include three maps to help you quickly and easily loop over a list of colors and their hex values.
$colors
lists all our available base (
500
) colors
$theme-colors
lists all semantically named theme colors (shown below)
$grays
lists all tints and shades of gray
Within
scss/_variables.scss
, you’ll find Bootstrap’s color variables and Sass map. Here’s an example of the
$colors
Sass map:
scss/_variables.scss
$colors
:
(
"blue"
:
$blue
,
"indigo"
:
$indigo
,
"purple"
:
$purple
,
"pink"
:
$pink
,
"red"
:
$red
,
"orange"
:
$orange
,
"yellow"
:
$yellow
,
"green"
:
$green
,
"teal"
:
$teal
,
"cyan"
:
$cyan
,
"black"
:
$black
,
"white"
:
$white
,
"gray"
:
$gray-600
,
"gray-dark"
:
$gray-800
)
;
Add, remove, or modify values within the map to update how they’re used in many other components. Unfortunately at this time, not
every
component utilizes this Sass map. Future updates will strive to improve upon this. Until then, plan on making use of the
${color}
variables and this Sass map.
Example
Here’s how you can use these in your Sass:
.alpha
{
color
:
$purple
;
}
.beta
{
color
:
$yellow-300
;
background-color
:
$indigo-900
;
}
Color
and
background
utility classes are also available for setting
color
and
background-color
using the
500
color values.
Generating utilities
Added in v5.1.0
Bootstrap doesn’t include
color
and
background-color
utilities for every color variable, but you can generate these yourself with our
utility API
and our extended Sass maps added in v5.1.0.
To start, make sure you’ve imported our functions, variables, mixins, and utilities.
Use our
map-merge-multiple()
function to quickly merge multiple Sass maps together in a new map.
Merge this new combined map to extend any utility with a
{color}-{level}
class name.
Here’s an example that generates text color utilities (e.g.,
.text-purple-500
) using the above steps.
@import
"bootstrap/scss/functions"
;
@import
"bootstrap/scss/variables"
;
@import
"bootstrap/scss/variables-dark"
;
@import
"bootstrap/scss/maps"
;
@import
"bootstrap/scss/mixins"
;
@import
"bootstrap/scss/utilities"
;
$all-colors
:
map-merge-multiple
(
$blues
,
$indigos
,
$purples
,
$pinks
,
$reds
,
$oranges
,
$yellows
,
$greens
,
$teals
,
$cyans
)
;
$utilities
:
map-merge
(
$utilities
,
(
"color"
:
map-merge
(
map-get
(
$utilities
,
"color"
)
,
(
values
:
map-merge
(
map-get
(
map-get
(
$utilities
,
"color"
)
,
"values"
)
,
(
$all-colors
)
,
)
,
)
,
)
,
)
)
;
@import
"bootstrap/scss/utilities/api"
;
This will generate new
.text-{color}-{level}
utilities for every color and level. You can do the same for any other utility and property as well.


## Color modes · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/customize/color-modes/
- fetched_at: 2026-04-29T13:46:02.705184+00:00

Added in v5.3
View on GitHub
Color modes
Bootstrap now supports color modes, or themes, as of v5.3.0. Explore our default light color mode and the new dark mode, or create your own using our styles as your template.
On this page
Try it yourself!
Download the source code and working demo for using Bootstrap with Stylelint, and the color modes from the
twbs/examples repository
. You can also
open the example in StackBlitz
.
Dark mode
Bootstrap now supports color modes, starting with dark mode!
With v5.3.0 you can implement your own color mode toggler (see below for an example from Bootstrap’s docs) and apply the different color modes as you see fit. We support a light mode (default) and now dark mode. Color modes can be toggled globally on the
<html>
element, or on specific components and elements, thanks to the
data-bs-theme
attribute.
Alternatively, you can also switch to a media query implementation thanks to our color mode mixin—see
the usage section for details
. Heads up though—this eliminates your ability to change themes on a per-component basis as shown below.
Example
For example, to change the color mode of a dropdown menu, add
data-bs-theme="light"
or
data-bs-theme="dark"
to the parent
.dropdown
. Now, no matter the global color mode, these dropdowns will display with the specified theme value.
Action
Action
Another action
Something else here
Separated link
Action
Action
Another action
Something else here
Separated link
html
<
div
class
=
"
dropdown
"
data-bs-theme
=
"
light
"
>
<
button
class
=
"
btn btn-secondary dropdown-toggle
"
type
=
"
button
"
id
=
"
dropdownMenuButtonLight
"
data-bs-toggle
=
"
dropdown
"
aria-expanded
=
"
false
"
>
Default dropdown
</
button
>
<
ul
class
=
"
dropdown-menu
"
aria-labelledby
=
"
dropdownMenuButtonLight
"
>
<
li
>
<
a
class
=
"
dropdown-item active
"
href
=
"
#
"
>
Action
</
a
>
</
li
>
<
li
>
<
a
class
=
"
dropdown-item
"
href
=
"
#
"
>
Action
</
a
>
</
li
>
<
li
>
<
a
class
=
"
dropdown-item
"
href
=
"
#
"
>
Another action
</
a
>
</
li
>
<
li
>
<
a
class
=
"
dropdown-item
"
href
=
"
#
"
>
Something else here
</
a
>
</
li
>
<
li
>
<
hr
class
=
"
dropdown-divider
"
>
</
li
>
<
li
>
<
a
class
=
"
dropdown-item
"
href
=
"
#
"
>
Separated link
</
a
>
</
li
>
</
ul
>
</
div
>
<
div
class
=
"
dropdown
"
data-bs-theme
=
"
dark
"
>
<
button
class
=
"
btn btn-secondary dropdown-toggle
"
type
=
"
button
"
id
=
"
dropdownMenuButtonDark
"
data-bs-toggle
=
"
dropdown
"
aria-expanded
=
"
false
"
>
Dark dropdown
</
button
>
<
ul
class
=
"
dropdown-menu
"
aria-labelledby
=
"
dropdownMenuButtonDark
"
>
<
li
>
<
a
class
=
"
dropdown-item active
"
href
=
"
#
"
>
Action
</
a
>
</
li
>
<
li
>
<
a
class
=
"
dropdown-item
"
href
=
"
#
"
>
Action
</
a
>
</
li
>
<
li
>
<
a
class
=
"
dropdown-item
"
href
=
"
#
"
>
Another action
</
a
>
</
li
>
<
li
>
<
a
class
=
"
dropdown-item
"
href
=
"
#
"
>
Something else here
</
a
>
</
li
>
<
li
>
<
hr
class
=
"
dropdown-divider
"
>
</
li
>
<
li
>
<
a
class
=
"
dropdown-item
"
href
=
"
#
"
>
Separated link
</
a
>
</
li
>
</
ul
>
</
div
>
How it works
As shown above, color mode styles are controlled by the
data-bs-theme
attribute. This attribute can be applied to the
<html>
element, or to any other element or Bootstrap component. If applied to the
<html>
element, it will apply to everything. If applied to a component or element, it will be scoped to that specific component or element.
For each color mode you wish to support, you’ll need to add new overrides for the shared global CSS variables. We do this already in our
_root.scss
stylesheet for dark mode, with light mode being the default values. In writing color mode specific styles, use the mixin:
// Color mode variables in _root.scss
@include
color-mode
(
dark
)
{
// CSS variable overrides here...
}
We use a custom
_variables-dark.scss
to power those shared global CSS variable overrides for dark mode. This file isn’t required for your own custom color modes, but it’s required for our dark mode for two reasons. First, it’s better to have a single place to reset global colors. Second, some Sass variables had to be overridden for background images embedded in our CSS for accordions, form components, and more.
Usage
Enable dark mode
Enable the built in dark color mode across your entire project by adding the
data-bs-theme="dark"
attribute to the
<html>
element. This will apply the dark color mode to all components and elements, other than those with a specific
data-bs-theme
attribute applied. Building on the
quick start template
:
<!
doctype
html
>
<
html
lang
=
"
en
"
data-bs-theme
=
"
dark
"
>
<
head
>
<
meta
charset
=
"
utf-8
"
>
<
meta
name
=
"
viewport
"
content
=
"
width=device-width, initial-scale=1
"
>
<
title
>
Bootstrap demo
</
title
>
<
link
href
=
"
https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css
"
rel
=
"
stylesheet
"
integrity
=
"
sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB
"
crossorigin
=
"
anonymous
"
>
</
head
>
<
body
>
<
h1
>
Hello, world!
</
h1
>
<
script
src
=
"
https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js
"
integrity
=
"
sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI
"
crossorigin
=
"
anonymous
"
>
</
script
>
</
body
>
</
html
>
Bootstrap does not yet ship with a built-in color mode picker, but you can use the one from our own documentation if you like.
Learn more in the JavaScript section.
Building with Sass
Our new dark mode option is available to use for all users of Bootstrap, but it’s controlled via data attributes instead of media queries and does not automatically toggle your project’s color mode. You can disable our dark mode entirely via Sass by changing
$enable-dark-mode
to
false
.
We use a custom Sass mixin,
color-mode()
, to help you control
how
color modes are applied. By default, we use a
data
attribute approach, allowing you to create more user-friendly experiences where your visitors can choose to have an automatic dark mode or control their preference (like in our own docs here). This is also an easy and scalable way to add different themes and more custom color modes beyond light and dark.
In case you want to use media queries and only make color modes automatic, you can change the mixin’s default type via Sass variable. Consider the following snippet and its compiled CSS output.
$color-mode-type
:
data
;
@include
color-mode
(
dark
)
{
.element
{
color
:
var
(
--bs-primary-text-emphasis
)
;
background-color
:
var
(
--bs-primary-bg-subtle
)
;
}
}
Outputs to:
[data-bs-theme=dark] .element
{
color
:
var
(
--bs-primary-text-emphasis
)
;
background-color
:
var
(
--bs-primary-bg-subtle
)
;
}
And when setting to
media-query
:
$color-mode-type
:
media-query
;
@include
color-mode
(
dark
)
{
.element
{
color
:
var
(
--bs-primary-text-emphasis
)
;
background-color
:
var
(
--bs-primary-bg-subtle
)
;
}
}
Outputs to:
@media
(
prefers-color-scheme
:
dark
)
{
.element
{
color
:
var
(
--bs-primary-text-emphasis
)
;
background-color
:
var
(
--bs-primary-bg-subtle
)
;
}
}
Custom color modes
While the primary use case for color modes is light and dark mode, custom color modes are also possible. Create your own
data-bs-theme
selector with a custom value as the name of your color mode, then modify our Sass and CSS variables as needed. We opted to create a separate
_variables-dark.scss
stylesheet to house Bootstrap’s dark mode specific Sass variables, but that’s not required for you.
For example, you can create a “blue theme” with the selector
data-bs-theme="blue"
. In your custom Sass or CSS file, add the new selector and override any global or component CSS variables as needed. If you’re using Sass, you can also use Sass’s functions within your CSS variable overrides.
site/src/scss/_content.scss
[data-bs-theme="blue"]
{
--bs-body-color
:
var
(
--bs-white
)
;
--bs-body-color-rgb
:
#
{
to-rgb
(
$white
)
}
;
--bs-body-bg
:
var
(
--bs-blue
)
;
--bs-body-bg-rgb
:
#
{
to-rgb
(
$blue
)
}
;
--bs-tertiary-bg
:
#{$blue-600}
;
.dropdown-menu
{
--bs-dropdown-bg
:
#
{
mix
(
$blue-500
,
$blue-600
)
}
;
--bs-dropdown-link-active-bg
:
#{$blue-700}
;
}
.btn-secondary
{
--bs-btn-bg
:
#
{
mix
(
$gray-600
,
$blue-400
,
.5
)
}
;
--bs-btn-border-color
:
#
{
rgba
(
$white
,
.25
)
}
;
--bs-btn-hover-bg
:
#
{
darken
(
mix
(
$gray-600
,
$blue-400
,
.5
)
,
5%
)
}
;
--bs-btn-hover-border-color
:
#
{
rgba
(
$white
,
.25
)
}
;
--bs-btn-active-bg
:
#
{
darken
(
mix
(
$gray-600
,
$blue-400
,
.5
)
,
10%
)
}
;
--bs-btn-active-border-color
:
#
{
rgba
(
$white
,
.5
)
}
;
--bs-btn-focus-border-color
:
#
{
rgba
(
$white
,
.5
)
}
;
--bs-btn-focus-box-shadow
:
0 0 0 .25rem
rgba
(
255
,
255
,
255
,
.2
)
;
}
}
Example blue theme
Some paragraph text to show how the blue theme might look with written copy.
Action
Action
Another action
Something else here
Separated link
<
div
data-bs-theme
=
"
blue
"
>
...
</
div
>
JavaScript
To allow visitors or users to toggle color modes, you’ll need to create a toggle element to control the
data-bs-theme
attribute on the root element,
<html>
. We’ve built a toggler in our documentation that initially defers to a user’s current system color mode, but provides an option to override that and pick a specific color mode.
Here’s a look at the JavaScript that powers it. Feel free to inspect our own documentation navbar to see how it’s implemented using HTML and CSS from our own components. It is suggested to include the JavaScript at the top of your page to reduce potential screen flickering during reloading of your site. Note that if you decide to use media queries for your color modes, your JavaScript may need to be modified or removed if you prefer an implicit control.
/*!
 * Color mode toggler for Bootstrap's docs (https://getbootstrap.com/)
 * Copyright 2011-2025 The Bootstrap Authors
 * Licensed under the Creative Commons Attribution 3.0 Unported License.
 */
(
(
)
=>
{
'use strict'
const
getStoredTheme
=
(
)
=>
localStorage
.
getItem
(
'theme'
)
const
setStoredTheme
=
theme
=>
localStorage
.
setItem
(
'theme'
,
theme
)
const
getPreferredTheme
=
(
)
=>
{
const
storedTheme
=
getStoredTheme
(
)
if
(
storedTheme
)
{
return
storedTheme
}
return
window
.
matchMedia
(
'(prefers-color-scheme: dark)'
)
.
matches
?
'dark'
:
'light'
}
const
setTheme
=
theme
=>
{
if
(
theme
===
'auto'
)
{
document
.
documentElement
.
setAttribute
(
'data-bs-theme'
,
(
window
.
matchMedia
(
'(prefers-color-scheme: dark)'
)
.
matches
?
'dark'
:
'light'
)
)
}
else
{
document
.
documentElement
.
setAttribute
(
'data-bs-theme'
,
theme
)
}
}
setTheme
(
getPreferredTheme
(
)
)
const
showActiveTheme
=
(
theme
,
focus
=
false
)
=>
{
const
themeSwitcher
=
document
.
querySelector
(
'#bd-theme'
)
if
(
!
themeSwitcher
)
{
return
}
const
themeSwitcherText
=
document
.
querySelector
(
'#bd-theme-text'
)
const
activeThemeIcon
=
document
.
querySelector
(
'.theme-icon-active use'
)
const
btnToActive
=
document
.
querySelector
(
`
[data-bs-theme-value="
${
theme
}
"]
`
)
const
svgOfActiveBtn
=
btnToActive
.
querySelector
(
'svg use'
)
.
getAttribute
(
'href'
)
document
.
querySelectorAll
(
'[data-bs-theme-value]'
)
.
forEach
(
element
=>
{
element
.
classList
.
remove
(
'active'
)
element
.
setAttribute
(
'aria-pressed'
,
'false'
)
}
)
btnToActive
.
classList
.
add
(
'active'
)
btnToActive
.
setAttribute
(
'aria-pressed'
,
'true'
)
activeThemeIcon
.
setAttribute
(
'href'
,
svgOfActiveBtn
)
const
themeSwitcherLabel
=
`
${
themeSwitcherText
.
textContent
}
(
${
btnToActive
.
dataset
.
bsThemeValue
}
)
`
themeSwitcher
.
setAttribute
(
'aria-label'
,
themeSwitcherLabel
)
if
(
focus
)
{
themeSwitcher
.
focus
(
)
}
}
window
.
matchMedia
(
'(prefers-color-scheme: dark)'
)
.
addEventListener
(
'change'
,
(
)
=>
{
const
storedTheme
=
getStoredTheme
(
)
if
(
storedTheme
!==
'light'
&&
storedTheme
!==
'dark'
)
{
setTheme
(
getPreferredTheme
(
)
)
}
}
)
window
.
addEventListener
(
'DOMContentLoaded'
,
(
)
=>
{
showActiveTheme
(
getPreferredTheme
(
)
)
document
.
querySelectorAll
(
'[data-bs-theme-value]'
)
.
forEach
(
toggle
=>
{
toggle
.
addEventListener
(
'click'
,
(
)
=>
{
const
theme
=
toggle
.
getAttribute
(
'data-bs-theme-value'
)
setStoredTheme
(
theme
)
setTheme
(
theme
)
showActiveTheme
(
theme
,
true
)
}
)
}
)
}
)
}
)
(
)
Adding theme colors
Adding a new color in
$theme-colors
is not enough for some of our components like
alerts
and
list groups
. New colors must also be defined in
$theme-colors-text
,
$theme-colors-bg-subtle
, and
$theme-colors-border-subtle
for light theme; but also in
$theme-colors-text-dark
,
$theme-colors-bg-subtle-dark
, and
$theme-colors-border-subtle-dark
for dark theme.
This is a manual process because Sass cannot generate its own Sass variables from an existing variable or map. In future versions of Bootstrap, we'll revisit this setup to reduce the duplication.
// Required
@import
"functions"
;
@import
"variables"
;
@import
"variables-dark"
;
// Add a custom color to $theme-colors
$custom-colors
:
(
"custom-color"
:
#712cf9
)
;
$theme-colors
:
map-merge
(
$theme-colors
,
$custom-colors
)
;
@import
"maps"
;
@import
"mixins"
;
@import
"utilities"
;
// Add a custom color to new theme maps
// Light mode
$custom-colors-text
:
(
"custom-color"
:
#712cf9
)
;
$custom-colors-bg-subtle
:
(
"custom-color"
:
#e1d2fe
)
;
$custom-colors-border-subtle
:
(
"custom-color"
:
#bfa1fc
)
;
$theme-colors-text
:
map-merge
(
$theme-colors-text
,
$custom-colors-text
)
;
$theme-colors-bg-subtle
:
map-merge
(
$theme-colors-bg-subtle
,
$custom-colors-bg-subtle
)
;
$theme-colors-border-subtle
:
map-merge
(
$theme-colors-border-subtle
,
$custom-colors-border-subtle
)
;
// Dark mode
$custom-colors-text-dark
:
(
"custom-color"
:
#e1d2f2
)
;
$custom-colors-bg-subtle-dark
:
(
"custom-color"
:
#8951fa
)
;
$custom-colors-border-subtle-dark
:
(
"custom-color"
:
#e1d2f2
)
;
$theme-colors-text-dark
:
map-merge
(
$theme-colors-text-dark
,
$custom-colors-text-dark
)
;
$theme-colors-bg-subtle-dark
:
map-merge
(
$theme-colors-bg-subtle-dark
,
$custom-colors-bg-subtle-dark
)
;
$theme-colors-border-subtle-dark
:
map-merge
(
$theme-colors-border-subtle-dark
,
$custom-colors-border-subtle-dark
)
;
// Remainder of Bootstrap imports
@import
"root"
;
@import
"reboot"
;
// etc
CSS
Variables
Dozens of root level CSS variables are repeated as overrides for dark mode. These are scoped to the color mode selector, which defaults to
data-bs-theme
but
can be configured
to use a
prefers-color-scheme
media query. Use these variables as a guideline for generating your own new color modes.
scss/_root.scss
--
#{$prefix}
body-color
:
#{$body-color-dark}
;
--
#{$prefix}
body-color-rgb
:
#
{
to-rgb
(
$body-color-dark
)
}
;
--
#{$prefix}
body-bg
:
#{$body-bg-dark}
;
--
#{$prefix}
body-bg-rgb
:
#
{
to-rgb
(
$body-bg-dark
)
}
;
--
#{$prefix}
emphasis-color
:
#{$body-emphasis-color-dark}
;
--
#{$prefix}
emphasis-color-rgb
:
#
{
to-rgb
(
$body-emphasis-color-dark
)
}
;
--
#{$prefix}
secondary-color
:
#{$body-secondary-color-dark}
;
--
#{$prefix}
secondary-color-rgb
:
#
{
to-rgb
(
$body-secondary-color-dark
)
}
;
--
#{$prefix}
secondary-bg
:
#{$body-secondary-bg-dark}
;
--
#{$prefix}
secondary-bg-rgb
:
#
{
to-rgb
(
$body-secondary-bg-dark
)
}
;
--
#{$prefix}
tertiary-color
:
#{$body-tertiary-color-dark}
;
--
#{$prefix}
tertiary-color-rgb
:
#
{
to-rgb
(
$body-tertiary-color-dark
)
}
;
--
#{$prefix}
tertiary-bg
:
#{$body-tertiary-bg-dark}
;
--
#{$prefix}
tertiary-bg-rgb
:
#
{
to-rgb
(
$body-tertiary-bg-dark
)
}
;
@each
$color
,
$value
in
$theme-colors-text-dark
{
--
#{$prefix}
#{$color}
-text-emphasis
:
#{$value}
;
}
@each
$color
,
$value
in
$theme-colors-bg-subtle-dark
{
--
#{$prefix}
#{$color}
-bg-subtle
:
#{$value}
;
}
@each
$color
,
$value
in
$theme-colors-border-subtle-dark
{
--
#{$prefix}
#{$color}
-border-subtle
:
#{$value}
;
}
--
#{$prefix}
heading-color
:
#{$headings-color-dark}
;
--
#{$prefix}
link-color
:
#{$link-color-dark}
;
--
#{$prefix}
link-hover-color
:
#{$link-hover-color-dark}
;
--
#{$prefix}
link-color-rgb
:
#
{
to-rgb
(
$link-color-dark
)
}
;
--
#{$prefix}
link-hover-color-rgb
:
#
{
to-rgb
(
$link-hover-color-dark
)
}
;
--
#{$prefix}
code-color
:
#{$code-color-dark}
;
--
#{$prefix}
highlight-color
:
#{$mark-color-dark}
;
--
#{$prefix}
highlight-bg
:
#{$mark-bg-dark}
;
--
#{$prefix}
border-color
:
#{$border-color-dark}
;
--
#{$prefix}
border-color-translucent
:
#{$border-color-translucent-dark}
;
--
#{$prefix}
form-valid-color
:
#{$form-valid-color-dark}
;
--
#{$prefix}
form-valid-border-color
:
#{$form-valid-border-color-dark}
;
--
#{$prefix}
form-invalid-color
:
#{$form-invalid-color-dark}
;
--
#{$prefix}
form-invalid-border-color
:
#{$form-invalid-border-color-dark}
;
Sass variables
CSS variables for our dark color mode are partially generated from dark mode specific Sass variables in
_variables-dark.scss
. This also includes some custom overrides for changing the colors of embedded SVGs used throughout our components.
scss/_variables-dark.scss
// scss-docs-start theme-text-dark-variables
$primary-text-emphasis-dark
:
tint-color
(
$primary
,
40%
)
;
$secondary-text-emphasis-dark
:
tint-color
(
$secondary
,
40%
)
;
$success-text-emphasis-dark
:
tint-color
(
$success
,
40%
)
;
$info-text-emphasis-dark
:
tint-color
(
$info
,
40%
)
;
$warning-text-emphasis-dark
:
tint-color
(
$warning
,
40%
)
;
$danger-text-emphasis-dark
:
tint-color
(
$danger
,
40%
)
;
$light-text-emphasis-dark
:
$gray-100
;
$dark-text-emphasis-dark
:
$gray-300
;
// scss-docs-end theme-text-dark-variables
// scss-docs-start theme-bg-subtle-dark-variables
$primary-bg-subtle-dark
:
shade-color
(
$primary
,
80%
)
;
$secondary-bg-subtle-dark
:
shade-color
(
$secondary
,
80%
)
;
$success-bg-subtle-dark
:
shade-color
(
$success
,
80%
)
;
$info-bg-subtle-dark
:
shade-color
(
$info
,
80%
)
;
$warning-bg-subtle-dark
:
shade-color
(
$warning
,
80%
)
;
$danger-bg-subtle-dark
:
shade-color
(
$danger
,
80%
)
;
$light-bg-subtle-dark
:
$gray-800
;
$dark-bg-subtle-dark
:
mix
(
$gray-800
,
$black
)
;
// scss-docs-end theme-bg-subtle-dark-variables
// scss-docs-start theme-border-subtle-dark-variables
$primary-border-subtle-dark
:
shade-color
(
$primary
,
40%
)
;
$secondary-border-subtle-dark
:
shade-color
(
$secondary
,
40%
)
;
$success-border-subtle-dark
:
shade-color
(
$success
,
40%
)
;
$info-border-subtle-dark
:
shade-color
(
$info
,
40%
)
;
$warning-border-subtle-dark
:
shade-color
(
$warning
,
40%
)
;
$danger-border-subtle-dark
:
shade-color
(
$danger
,
40%
)
;
$light-border-subtle-dark
:
$gray-700
;
$dark-border-subtle-dark
:
$gray-800
;
// scss-docs-end theme-border-subtle-dark-variables
$body-color-dark
:
$gray-300
;
$body-bg-dark
:
$gray-900
;
$body-secondary-color-dark
:
rgba
(
$body-color-dark
,
.75
)
;
$body-secondary-bg-dark
:
$gray-800
;
$body-tertiary-color-dark
:
rgba
(
$body-color-dark
,
.5
)
;
$body-tertiary-bg-dark
:
mix
(
$gray-800
,
$gray-900
,
50%
)
;
$body-emphasis-color-dark
:
$white
;
$border-color-dark
:
$gray-700
;
$border-color-translucent-dark
:
rgba
(
$white
,
.15
)
;
$headings-color-dark
:
inherit
;
$link-color-dark
:
tint-color
(
$primary
,
40%
)
;
$link-hover-color-dark
:
shift-color
(
$link-color-dark
,
-
$link-shade-percentage
)
;
$code-color-dark
:
tint-color
(
$code-color
,
40%
)
;
$mark-color-dark
:
$body-color-dark
;
$mark-bg-dark
:
$yellow-800
;
//
// Forms
//
$form-select-indicator-color-dark
:
$body-color-dark
;
$form-select-indicator-dark
:
url
(
"data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'><path fill='none' stroke='#{$form-select-indicator-color-dark}' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='m2 5 6 6 6-6'/></svg>"
)
;
$form-switch-color-dark
:
rgba
(
$white
,
.25
)
;
$form-switch-bg-image-dark
:
url
(
"data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'><circle r='3' fill='#{$form-switch-color-dark}'/></svg>"
)
;
// scss-docs-start form-validation-colors-dark
$form-valid-color-dark
:
$green-300
;
$form-valid-border-color-dark
:
$green-300
;
$form-invalid-color-dark
:
$red-300
;
$form-invalid-border-color-dark
:
$red-300
;
// scss-docs-end form-validation-colors-dark
//
// Accordion
//
$accordion-icon-color-dark
:
$primary-text-emphasis-dark
;
$accordion-icon-active-color-dark
:
$primary-text-emphasis-dark
;
$accordion-button-icon-dark
:
url
(
"data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='#{$accordion-icon-color-dark}'><path fill-rule='evenodd' d='M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708'/></svg>"
)
;
$accordion-button-active-icon-dark
:
url
(
"data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='#{$accordion-icon-active-color-dark}'><path fill-rule='evenodd' d='M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708'/></svg>"
)
;
Sass mixins
Styles for dark mode, and any custom color modes you create, can be scoped appropriately to the
data-bs-theme
attribute selector or media query with the customizable
color-mode()
mixin. See the
Sass usage section
for more details.
scss/mixins/_color-mode.scss
@mixin
color-mode
(
$mode
:
light
,
$root
:
false
)
{
@if
$color-mode-type
== "media-query"
{
@if
$root
== true
{
@media
(
prefers-color-scheme
:
$mode
)
{
:root
{
@content
;
}
}
}
@else
{
@media
(
prefers-color-scheme
:
$mode
)
{
@content
;
}
}
}
@else
{
[data-bs-theme="
#{$mode}
"]
{
@content
;
}
}
}


## Components · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/customize/components/
- fetched_at: 2026-04-29T13:46:03.053835+00:00

View on GitHub
Components
Learn how and why we build nearly all our components responsively and with base and modifier classes.
On this page
Base classes
Bootstrap’s components are largely built with a base-modifier nomenclature. We group as many shared properties as possible into a base class, like
.btn
, and then group individual styles for each variant into modifier classes, like
.btn-primary
or
.btn-success
.
To build our modifier classes, we use Sass’s
@each
loops to iterate over a Sass map. This is especially helpful for generating variants of a component by our
$theme-colors
and creating responsive variants for each breakpoint. As you customize these Sass maps and recompile, you’ll automatically see your changes reflected in these loops.
Check out
our Sass maps and loops docs
for how to customize these loops and extend Bootstrap’s base-modifier approach to your own code.
Modifiers
Many of Bootstrap’s components are built with a base-modifier class approach. This means the bulk of the styling is contained to a base class (e.g.,
.btn
) while style variations are confined to modifier classes (e.g.,
.btn-danger
). These modifier classes are built from the
$theme-colors
map to make customizing the number and name of our modifier classes.
Here are two examples of how we loop over the
$theme-colors
map to generate modifiers to the
.alert
and
.list-group
components.
scss/_alert.scss
// Generate contextual modifier classes for colorizing the alert
@each
$state
in
map-keys
(
$theme-colors
)
{
.alert-
#{$state}
{
--
#{$prefix}
alert-color
:
var
(
--
#{$prefix}
#{$state}
-text-emphasis
)
;
--
#{$prefix}
alert-bg
:
var
(
--
#{$prefix}
#{$state}
-bg-subtle
)
;
--
#{$prefix}
alert-border-color
:
var
(
--
#{$prefix}
#{$state}
-border-subtle
)
;
--
#{$prefix}
alert-link-color
:
var
(
--
#{$prefix}
#{$state}
-text-emphasis
)
;
}
}
scss/_list-group.scss
// List group contextual variants
//
// Add modifier classes to change text and background color on individual items.
// Organizationally, this must come after the `:hover` states.
@each
$state
in
map-keys
(
$theme-colors
)
{
.list-group-item-
#{$state}
{
--
#{$prefix}
list-group-color
:
var
(
--
#{$prefix}
#{$state}
-text-emphasis
)
;
--
#{$prefix}
list-group-bg
:
var
(
--
#{$prefix}
#{$state}
-bg-subtle
)
;
--
#{$prefix}
list-group-border-color
:
var
(
--
#{$prefix}
#{$state}
-border-subtle
)
;
--
#{$prefix}
list-group-action-hover-color
:
var
(
--
#{$prefix}
emphasis-color
)
;
--
#{$prefix}
list-group-action-hover-bg
:
var
(
--
#{$prefix}
#{$state}
-border-subtle
)
;
--
#{$prefix}
list-group-action-active-color
:
var
(
--
#{$prefix}
emphasis-color
)
;
--
#{$prefix}
list-group-action-active-bg
:
var
(
--
#{$prefix}
#{$state}
-border-subtle
)
;
--
#{$prefix}
list-group-active-color
:
var
(
--
#{$prefix}
#{$state}
-bg-subtle
)
;
--
#{$prefix}
list-group-active-bg
:
var
(
--
#{$prefix}
#{$state}
-text-emphasis
)
;
--
#{$prefix}
list-group-active-border-color
:
var
(
--
#{$prefix}
#{$state}
-text-emphasis
)
;
}
}
Responsive
These Sass loops aren’t limited to color maps, either. You can also generate responsive variations of your components. Take for example our responsive alignment of the dropdowns where we mix an
@each
loop for the
$grid-breakpoints
Sass map with a media query include.
scss/_dropdown.scss
// We deliberately hardcode the `bs-` prefix because we check
// this custom property in JS to determine Popper's positioning
@each
$breakpoint
in
map-keys
(
$grid-breakpoints
)
{
@include
media-breakpoint-up
(
$breakpoint
)
{
$infix
:
breakpoint-infix
(
$breakpoint
,
$grid-breakpoints
)
;
.dropdown-menu
#{$infix}
-start
{
--bs-position
:
start
;
&
[data-bs-popper]
{
right
:
auto
;
left
:
0
;
}
}
.dropdown-menu
#{$infix}
-end
{
--bs-position
:
end
;
&
[data-bs-popper]
{
right
:
0
;
left
:
auto
;
}
}
}
}
Should you modify your
$grid-breakpoints
, your changes will apply to all the loops iterating over that map.
scss/_variables.scss
$grid-breakpoints
:
(
xs
:
0
,
sm
:
576px
,
md
:
768px
,
lg
:
992px
,
xl
:
1200px
,
xxl
:
1400px
)
;
For more information and examples on how to modify our Sass maps and variables, please refer to
the CSS section of the Grid documentation
.
Creating your own
We encourage you to adopt these guidelines when building with Bootstrap to create your own components. We’ve extended this approach ourselves to the custom components in our documentation and examples. Components like our callouts are built just like our provided components with base and modifier classes.
This is a callout.
We built it custom for our docs so our messages to you stand out. It has three variants via modifier classes.
<
div
class
=
"
callout
"
>
...
</
div
>
In your CSS, you’d have something like the following where the bulk of the styling is done via
.callout
. Then, the unique styles between each variant is controlled via modifier class.
// Base class
.callout
{
}
// Modifier classes
.callout-info
{
}
.callout-warning
{
}
.callout-danger
{
}
For the callouts, that unique styling is just a
border-left-color
. When you combine that base class with one of those modifier classes, you get your complete component family:
This is an info callout.
Example text to show it in action.
This is a warning callout.
Example text to show it in action.
This is a danger callout.
Example text to show it in action.


## Optimize · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/customize/optimize/
- fetched_at: 2026-04-29T13:46:03.405578+00:00

View on GitHub
Optimize
Keep your projects lean, responsive, and maintainable so you can deliver the best experience and focus on more important jobs.
On this page
Lean Sass imports
When using Sass in your asset pipeline, make sure you optimize Bootstrap by only
@import
ing the components you need. Your largest optimizations will likely come from the
Layout & Components
section of our
bootstrap.scss
.
scss/bootstrap.scss
// Configuration
@import
"functions"
;
@import
"variables"
;
@import
"variables-dark"
;
@import
"maps"
;
@import
"mixins"
;
@import
"utilities"
;
// Layout & components
@import
"root"
;
@import
"reboot"
;
@import
"type"
;
@import
"images"
;
@import
"containers"
;
@import
"grid"
;
@import
"tables"
;
@import
"forms"
;
@import
"buttons"
;
@import
"transitions"
;
@import
"dropdown"
;
@import
"button-group"
;
@import
"nav"
;
@import
"navbar"
;
@import
"card"
;
@import
"accordion"
;
@import
"breadcrumb"
;
@import
"pagination"
;
@import
"badge"
;
@import
"alert"
;
@import
"progress"
;
@import
"list-group"
;
@import
"close"
;
@import
"toasts"
;
@import
"modal"
;
@import
"tooltip"
;
@import
"popover"
;
@import
"carousel"
;
@import
"spinners"
;
@import
"offcanvas"
;
@import
"placeholders"
;
// Helpers
@import
"helpers"
;
// Utilities
@import
"utilities/api"
;
If you’re not using a component, comment it out or delete it entirely. For example, if you’re not using the carousel, remove that import to save some file size in your compiled CSS. Keep in mind there are some dependencies across Sass imports that may make it more difficult to omit a file.
Lean JavaScript
Bootstrap’s JavaScript includes every component in our primary dist files (
bootstrap.js
and
bootstrap.min.js
), and even our primary dependency (Popper) with our bundle files (
bootstrap.bundle.js
and
bootstrap.bundle.min.js
). While you’re customizing via Sass, be sure to remove related JavaScript.
For instance, assuming you’re using your own JavaScript bundler like Webpack, Parcel, or Vite, you’d only import the JavaScript you plan on using. In the example below, we show how to just include our modal JavaScript:
// Import just what we need
// import 'bootstrap/js/dist/alert';
// import 'bootstrap/js/dist/button';
// import 'bootstrap/js/dist/carousel';
// import 'bootstrap/js/dist/collapse';
// import 'bootstrap/js/dist/dropdown';
import
'bootstrap/js/dist/modal'
;
// import 'bootstrap/js/dist/offcanvas';
// import 'bootstrap/js/dist/popover';
// import 'bootstrap/js/dist/scrollspy';
// import 'bootstrap/js/dist/tab';
// import 'bootstrap/js/dist/toast';
// import 'bootstrap/js/dist/tooltip';
This way, you’re not including any JavaScript you don’t intend to use for components like buttons, carousels, and tooltips. If you’re importing dropdowns, tooltips or popovers, be sure to list the Popper dependency in your
package.json
file.
Heads up!
Files in
bootstrap/js/dist
use the
default export
. To use them, do the following:
import
Modal
from
'bootstrap/js/dist/modal'
const
modal
=
new
Modal
(
document
.
getElementById
(
'myModal'
)
)
Autoprefixer .browserslistrc
Bootstrap depends on Autoprefixer to automatically add browser prefixes to certain CSS properties. Prefixes are dictated by our
.browserslistrc
file, found in the root of the Bootstrap repo. Customizing this list of browsers and recompiling the Sass will automatically remove some CSS from your compiled CSS, if there are vendor prefixes unique to that browser or version.
Unused CSS
Help wanted with this section, please consider opening a PR. Thanks!
While we don’t have a prebuilt example for using
PurgeCSS
with Bootstrap, there are some helpful articles and walkthroughs that the community has written. Here are some options:
https://medium.com/dwarves-foundation/remove-unused-css-styles-from-bootstrap-using-purgecss-88395a2c5772
https://lukelowrey.com/automatically-removeunused-css-from-bootstrap-or-other-frameworks/
Lastly, this
CSS Tricks article on unused CSS
shows how to use PurgeCSS and other similar tools.
Minify and gzip
Whenever possible, be sure to compress all the code you serve to your visitors. If you’re using Bootstrap dist files, try to stick to the minified versions (indicated by the
.min.css
and
.min.js
extensions). If you’re building Bootstrap from the source with your own build system, be sure to implement your own minifiers for HTML, CSS, and JS.
Non-blocking files
While minifying and using compression might seem like enough, making your files non-blocking ones is also a big step in making your site well-optimized and fast enough.
If you are using a
Lighthouse
plugin in Google Chrome, you may have stumbled over FCP.
The First Contentful Paint
metric measures the time from when the page starts loading to when any part of the page’s content is rendered on the screen.
You can improve FCP by deferring non-critical JavaScript or CSS. What does that mean? Simply, JavaScript or stylesheets that don’t need to be present on the first paint of your page should be marked with
async
or
defer
attributes.
This ensures that the less important resources are loaded later and not blocking the first paint. On the other hand, critical resources can be included as inline scripts or styles.
If you want to learn more about this, there are already a lot of great articles about it:
https://developer.chrome.com/docs/lighthouse/performance/render-blocking-resources/
https://web.dev/articles/defer-non-critical-css
Always use HTTPS
Your website should only be available over HTTPS connections in production. HTTPS improves the security, privacy, and availability of all sites, and
there is no such thing as non-sensitive web traffic
. The steps to configure your website to be served exclusively over HTTPS vary widely depending on your architecture and web hosting provider, and thus are beyond the scope of these docs.
Sites served over HTTPS should also access all stylesheets, scripts, and other assets over HTTPS connections. Otherwise, you’ll be sending users
mixed active content
, leading to potential vulnerabilities where a site can be compromised by altering a dependency. This can lead to security issues and in-browser warnings displayed to users. Whether you’re getting Bootstrap from a CDN or serving it yourself, ensure that you only access it over HTTPS connections.


## Form controls · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/forms/form-control/
- fetched_at: 2026-04-29T13:46:03.643094+00:00

View on GitHub
Form controls
Give textual form controls like
<input>
s and
<textarea>
s an upgrade with custom styles, sizing, focus states, and more.
On this page
Example
Form controls are styled with a mix of Sass and CSS variables, allowing them to adapt to color modes and support any customization method.
Email address
Example textarea
html
<
div
class
=
"
mb-3
"
>
<
label
for
=
"
exampleFormControlInput1
"
class
=
"
form-label
"
>
Email address
</
label
>
<
input
type
=
"
email
"
class
=
"
form-control
"
id
=
"
exampleFormControlInput1
"
placeholder
=
"
name@example.com
"
>
</
div
>
<
div
class
=
"
mb-3
"
>
<
label
for
=
"
exampleFormControlTextarea1
"
class
=
"
form-label
"
>
Example textarea
</
label
>
<
textarea
class
=
"
form-control
"
id
=
"
exampleFormControlTextarea1
"
rows
=
"
3
"
>
</
textarea
>
</
div
>
Sizing
Set heights using classes like
.form-control-lg
and
.form-control-sm
.
html
<
input
class
=
"
form-control form-control-lg
"
type
=
"
text
"
placeholder
=
"
.form-control-lg
"
aria-label
=
"
.form-control-lg example
"
>
<
input
class
=
"
form-control
"
type
=
"
text
"
placeholder
=
"
Default input
"
aria-label
=
"
default input example
"
>
<
input
class
=
"
form-control form-control-sm
"
type
=
"
text
"
placeholder
=
"
.form-control-sm
"
aria-label
=
"
.form-control-sm example
"
>
Form text
Block-level or inline-level form text can be created using
.form-text
.
Form text should be explicitly associated with the form control it relates to using the
aria-describedby
attribute. This will ensure that assistive technologies—such as screen readers—will announce this form text when the user focuses or enters the control.
Form text below inputs can be styled with
.form-text
. If a block-level element will be used, a top margin is added for easy spacing from the inputs above.
Password
Your password must be 8-20 characters long, contain letters and numbers, and must not contain spaces, special characters, or emoji.
html
<
label
for
=
"
inputPassword5
"
class
=
"
form-label
"
>
Password
</
label
>
<
input
type
=
"
password
"
id
=
"
inputPassword5
"
class
=
"
form-control
"
aria-describedby
=
"
passwordHelpBlock
"
>
<
div
id
=
"
passwordHelpBlock
"
class
=
"
form-text
"
>
Your password must be 8-20 characters long, contain letters and numbers, and must not contain spaces, special characters, or emoji.
</
div
>
Inline text can use any typical inline HTML element (be it a
<span>
,
<small>
, or something else) with nothing more than the
.form-text
class.
Password
Must be 8-20 characters long.
html
<
div
class
=
"
row g-3 align-items-center
"
>
<
div
class
=
"
col-auto
"
>
<
label
for
=
"
inputPassword6
"
class
=
"
col-form-label
"
>
Password
</
label
>
</
div
>
<
div
class
=
"
col-auto
"
>
<
input
type
=
"
password
"
id
=
"
inputPassword6
"
class
=
"
form-control
"
aria-describedby
=
"
passwordHelpInline
"
>
</
div
>
<
div
class
=
"
col-auto
"
>
<
span
id
=
"
passwordHelpInline
"
class
=
"
form-text
"
>
Must be 8-20 characters long.
</
span
>
</
div
>
</
div
>
Disabled
Add the
disabled
boolean attribute on an input to give it a grayed out appearance, remove pointer events, and prevent focusing.
html
<
input
class
=
"
form-control
"
type
=
"
text
"
placeholder
=
"
Disabled input
"
aria-label
=
"
Disabled input example
"
disabled
>
<
input
class
=
"
form-control
"
type
=
"
text
"
value
=
"
Disabled readonly input
"
aria-label
=
"
Disabled input example
"
disabled
readonly
>
Readonly
Add the
readonly
boolean attribute on an input to prevent modification of the input’s value.
readonly
inputs can still be focused and selected, while
disabled
inputs cannot.
html
<
input
class
=
"
form-control
"
type
=
"
text
"
value
=
"
Readonly input here...
"
aria-label
=
"
readonly input example
"
readonly
>
Readonly plain text
If you want to have
<input readonly>
elements in your form styled as plain text, replace
.form-control
with
.form-control-plaintext
to remove the default form field styling and preserve the correct
margin
and
padding
.
Email
Password
html
<
div
class
=
"
mb-3 row
"
>
<
label
for
=
"
staticEmail
"
class
=
"
col-sm-2 col-form-label
"
>
Email
</
label
>
<
div
class
=
"
col-sm-10
"
>
<
input
type
=
"
text
"
readonly
class
=
"
form-control-plaintext
"
id
=
"
staticEmail
"
value
=
"
email@example.com
"
>
</
div
>
</
div
>
<
div
class
=
"
mb-3 row
"
>
<
label
for
=
"
inputPassword
"
class
=
"
col-sm-2 col-form-label
"
>
Password
</
label
>
<
div
class
=
"
col-sm-10
"
>
<
input
type
=
"
password
"
class
=
"
form-control
"
id
=
"
inputPassword
"
>
</
div
>
</
div
>
html
<
form
class
=
"
row g-3
"
>
<
div
class
=
"
col-auto
"
>
<
label
for
=
"
staticEmail2
"
class
=
"
visually-hidden
"
>
Email
</
label
>
<
input
type
=
"
text
"
readonly
class
=
"
form-control-plaintext
"
id
=
"
staticEmail2
"
value
=
"
email@example.com
"
>
</
div
>
<
div
class
=
"
col-auto
"
>
<
label
for
=
"
inputPassword2
"
class
=
"
visually-hidden
"
>
Password
</
label
>
<
input
type
=
"
password
"
class
=
"
form-control
"
id
=
"
inputPassword2
"
placeholder
=
"
Password
"
>
</
div
>
<
div
class
=
"
col-auto
"
>
<
button
type
=
"
submit
"
class
=
"
btn btn-primary mb-3
"
>
Confirm identity
</
button
>
</
div
>
</
form
>
File input
Default file input example
Multiple files input example
Disabled file input example
Small file input example
Large file input example
html
<
div
class
=
"
mb-3
"
>
<
label
for
=
"
formFile
"
class
=
"
form-label
"
>
Default file input example
</
label
>
<
input
class
=
"
form-control
"
type
=
"
file
"
id
=
"
formFile
"
>
</
div
>
<
div
class
=
"
mb-3
"
>
<
label
for
=
"
formFileMultiple
"
class
=
"
form-label
"
>
Multiple files input example
</
label
>
<
input
class
=
"
form-control
"
type
=
"
file
"
id
=
"
formFileMultiple
"
multiple
>
</
div
>
<
div
class
=
"
mb-3
"
>
<
label
for
=
"
formFileDisabled
"
class
=
"
form-label
"
>
Disabled file input example
</
label
>
<
input
class
=
"
form-control
"
type
=
"
file
"
id
=
"
formFileDisabled
"
disabled
>
</
div
>
<
div
class
=
"
mb-3
"
>
<
label
for
=
"
formFileSm
"
class
=
"
form-label
"
>
Small file input example
</
label
>
<
input
class
=
"
form-control form-control-sm
"
id
=
"
formFileSm
"
type
=
"
file
"
>
</
div
>
<
div
>
<
label
for
=
"
formFileLg
"
class
=
"
form-label
"
>
Large file input example
</
label
>
<
input
class
=
"
form-control form-control-lg
"
id
=
"
formFileLg
"
type
=
"
file
"
>
</
div
>
Color
Set the
type="color"
and add
.form-control-color
to the
<input>
. We use the modifier class to set fixed
height
s and override some inconsistencies between browsers.
Color picker
html
<
label
for
=
"
exampleColorInput
"
class
=
"
form-label
"
>
Color picker
</
label
>
<
input
type
=
"
color
"
class
=
"
form-control form-control-color
"
id
=
"
exampleColorInput
"
value
=
"
#563d7c
"
title
=
"
Choose your color
"
>
Datalists
Datalists allow you to create a group of
<option>
s that can be accessed (and autocompleted) from within an
<input>
. These are similar to
<select>
elements, but come with more menu styling limitations and differences. While most browsers and operating systems include some support for
<datalist>
elements, their styling is inconsistent at best.
Learn more about
support for datalist elements
.
Datalist example
html
<
label
for
=
"
exampleDataList
"
class
=
"
form-label
"
>
Datalist example
</
label
>
<
input
class
=
"
form-control
"
list
=
"
datalistOptions
"
id
=
"
exampleDataList
"
placeholder
=
"
Type to search...
"
>
<
datalist
id
=
"
datalistOptions
"
>
<
option
value
=
"
San Francisco
"
>
<
option
value
=
"
New York
"
>
<
option
value
=
"
Seattle
"
>
<
option
value
=
"
Los Angeles
"
>
<
option
value
=
"
Chicago
"
>
</
datalist
>
CSS
Sass variables
$input-*
are shared across most of our form controls (and not buttons).
scss/_variables.scss
$input-padding-y
:
$input-btn-padding-y
;
$input-padding-x
:
$input-btn-padding-x
;
$input-font-family
:
$input-btn-font-family
;
$input-font-size
:
$input-btn-font-size
;
$input-font-weight
:
$font-weight-base
;
$input-line-height
:
$input-btn-line-height
;
$input-padding-y-sm
:
$input-btn-padding-y-sm
;
$input-padding-x-sm
:
$input-btn-padding-x-sm
;
$input-font-size-sm
:
$input-btn-font-size-sm
;
$input-padding-y-lg
:
$input-btn-padding-y-lg
;
$input-padding-x-lg
:
$input-btn-padding-x-lg
;
$input-font-size-lg
:
$input-btn-font-size-lg
;
$input-bg
:
var
(
--
#{$prefix}
body-bg
)
;
$input-disabled-color
:
null
;
$input-disabled-bg
:
var
(
--
#{$prefix}
secondary-bg
)
;
$input-disabled-border-color
:
null
;
$input-color
:
var
(
--
#{$prefix}
body-color
)
;
$input-border-color
:
var
(
--
#{$prefix}
border-color
)
;
$input-border-width
:
$input-btn-border-width
;
$input-box-shadow
:
var
(
--
#{$prefix}
box-shadow-inset
)
;
$input-border-radius
:
var
(
--
#{$prefix}
border-radius
)
;
$input-border-radius-sm
:
var
(
--
#{$prefix}
border-radius-sm
)
;
$input-border-radius-lg
:
var
(
--
#{$prefix}
border-radius-lg
)
;
$input-focus-bg
:
$input-bg
;
$input-focus-border-color
:
tint-color
(
$component-active-bg
,
50%
)
;
$input-focus-color
:
$input-color
;
$input-focus-width
:
$input-btn-focus-width
;
$input-focus-box-shadow
:
$input-btn-focus-box-shadow
;
$input-placeholder-color
:
var
(
--
#{$prefix}
secondary-color
)
;
$input-plaintext-color
:
var
(
--
#{$prefix}
body-color
)
;
$input-height-border
:
calc
(
#{$input-border-width}
*
2
)
;
// stylelint-disable-line function-disallowed-list
$input-height-inner
:
add
(
$input-line-height
*
1em
,
$input-padding-y
*
2
)
;
$input-height-inner-half
:
add
(
$input-line-height
*
.5em
,
$input-padding-y
)
;
$input-height-inner-quarter
:
add
(
$input-line-height
*
.25em
,
$input-padding-y
*
.5
)
;
$input-height
:
add
(
$input-line-height
*
1em
,
add
(
$input-padding-y
*
2
,
$input-height-border
,
false
)
)
;
$input-height-sm
:
add
(
$input-line-height
*
1em
,
add
(
$input-padding-y-sm
*
2
,
$input-height-border
,
false
)
)
;
$input-height-lg
:
add
(
$input-line-height
*
1em
,
add
(
$input-padding-y-lg
*
2
,
$input-height-border
,
false
)
)
;
$input-transition
:
border-color .15s ease-in-out
,
box-shadow .15s ease-in-out
;
$form-color-width
:
3rem
;
$form-label-*
and
$form-text-*
are for our
<label>
s and
.form-text
component.
scss/_variables.scss
$form-label-margin-bottom
:
.5rem
;
$form-label-font-size
:
null
;
$form-label-font-style
:
null
;
$form-label-font-weight
:
null
;
$form-label-color
:
null
;
scss/_variables.scss
$form-text-margin-top
:
.25rem
;
$form-text-font-size
:
$small-font-size
;
$form-text-font-style
:
null
;
$form-text-font-weight
:
null
;
$form-text-color
:
var
(
--
#{$prefix}
secondary-color
)
;
$form-file-*
are for file input.
scss/_variables.scss
$form-file-button-color
:
$input-color
;
$form-file-button-bg
:
var
(
--
#{$prefix}
tertiary-bg
)
;
$form-file-button-hover-bg
:
var
(
--
#{$prefix}
secondary-bg
)
;


## Select · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/forms/select/
- fetched_at: 2026-04-29T13:46:03.847613+00:00

View on GitHub
Select
Customize the native
<select>
s with custom CSS that changes the element’s initial appearance.
On this page
Default
Custom
<select>
menus need only a custom class,
.form-select
to trigger the custom styles. Custom styles are limited to the
<select>
’s initial appearance and cannot modify the
<option>
s due to browser limitations.
Open this select menu
One
Two
Three
html
<
select
class
=
"
form-select
"
aria-label
=
"
Default select example
"
>
<
option
selected
>
Open this select menu
</
option
>
<
option
value
=
"
1
"
>
One
</
option
>
<
option
value
=
"
2
"
>
Two
</
option
>
<
option
value
=
"
3
"
>
Three
</
option
>
</
select
>
Sizing
You may also choose from small and large custom selects to match our similarly sized text inputs.
Open this select menu
One
Two
Three
Open this select menu
One
Two
Three
html
<
select
class
=
"
form-select form-select-lg mb-3
"
aria-label
=
"
Large select example
"
>
<
option
selected
>
Open this select menu
</
option
>
<
option
value
=
"
1
"
>
One
</
option
>
<
option
value
=
"
2
"
>
Two
</
option
>
<
option
value
=
"
3
"
>
Three
</
option
>
</
select
>
<
select
class
=
"
form-select form-select-sm
"
aria-label
=
"
Small select example
"
>
<
option
selected
>
Open this select menu
</
option
>
<
option
value
=
"
1
"
>
One
</
option
>
<
option
value
=
"
2
"
>
Two
</
option
>
<
option
value
=
"
3
"
>
Three
</
option
>
</
select
>
The
multiple
attribute is also supported:
Open this select menu
One
Two
Three
html
<
select
class
=
"
form-select
"
multiple
aria-label
=
"
Multiple select example
"
>
<
option
selected
>
Open this select menu
</
option
>
<
option
value
=
"
1
"
>
One
</
option
>
<
option
value
=
"
2
"
>
Two
</
option
>
<
option
value
=
"
3
"
>
Three
</
option
>
</
select
>
As is the
size
attribute:
Open this select menu
One
Two
Three
html
<
select
class
=
"
form-select
"
size
=
"
3
"
aria-label
=
"
Size 3 select example
"
>
<
option
selected
>
Open this select menu
</
option
>
<
option
value
=
"
1
"
>
One
</
option
>
<
option
value
=
"
2
"
>
Two
</
option
>
<
option
value
=
"
3
"
>
Three
</
option
>
</
select
>
Disabled
Add the
disabled
boolean attribute on a select to give it a grayed out appearance and remove pointer events.
Open this select menu
One
Two
Three
html
<
select
class
=
"
form-select
"
aria-label
=
"
Disabled select example
"
disabled
>
<
option
selected
>
Open this select menu
</
option
>
<
option
value
=
"
1
"
>
One
</
option
>
<
option
value
=
"
2
"
>
Two
</
option
>
<
option
value
=
"
3
"
>
Three
</
option
>
</
select
>
CSS
Sass variables
scss/_variables.scss
$form-select-padding-y
:
$input-padding-y
;
$form-select-padding-x
:
$input-padding-x
;
$form-select-font-family
:
$input-font-family
;
$form-select-font-size
:
$input-font-size
;
$form-select-indicator-padding
:
$form-select-padding-x
*
3
;
// Extra padding for background-image
$form-select-font-weight
:
$input-font-weight
;
$form-select-line-height
:
$input-line-height
;
$form-select-color
:
$input-color
;
$form-select-bg
:
$input-bg
;
$form-select-disabled-color
:
null
;
$form-select-disabled-bg
:
$input-disabled-bg
;
$form-select-disabled-border-color
:
$input-disabled-border-color
;
$form-select-bg-position
:
right
$form-select-padding-x
center
;
$form-select-bg-size
:
16px 12px
;
// In pixels because image dimensions
$form-select-indicator-color
:
$gray-800
;
$form-select-indicator
:
url
(
"data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'><path fill='none' stroke='#{$form-select-indicator-color}' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='m2 5 6 6 6-6'/></svg>"
)
;
$form-select-feedback-icon-padding-end
:
$form-select-padding-x
*
2.5
+
$form-select-indicator-padding
;
$form-select-feedback-icon-position
:
center right
$form-select-indicator-padding
;
$form-select-feedback-icon-size
:
$input-height-inner-half
$input-height-inner-half
;
$form-select-border-width
:
$input-border-width
;
$form-select-border-color
:
$input-border-color
;
$form-select-border-radius
:
$input-border-radius
;
$form-select-box-shadow
:
var
(
--
#{$prefix}
box-shadow-inset
)
;
$form-select-focus-border-color
:
$input-focus-border-color
;
$form-select-focus-width
:
$input-focus-width
;
$form-select-focus-box-shadow
:
0 0 0
$form-select-focus-width
$input-btn-focus-color
;
$form-select-padding-y-sm
:
$input-padding-y-sm
;
$form-select-padding-x-sm
:
$input-padding-x-sm
;
$form-select-font-size-sm
:
$input-font-size-sm
;
$form-select-border-radius-sm
:
$input-border-radius-sm
;
$form-select-padding-y-lg
:
$input-padding-y-lg
;
$form-select-padding-x-lg
:
$input-padding-x-lg
;
$form-select-font-size-lg
:
$input-font-size-lg
;
$form-select-border-radius-lg
:
$input-border-radius-lg
;
$form-select-transition
:
$input-transition
;


## Checks and radios · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/forms/checks-radios/
- fetched_at: 2026-04-29T13:46:04.192120+00:00

View on GitHub
Checks and radios
Create consistent cross-browser and cross-device checkboxes and radios with our completely rewritten checks component.
On this page
Approach
Browser default checkboxes and radios are replaced with the help of
.form-check
, a series of classes for both input types that improves the layout and behavior of their HTML elements, that provide greater customization and cross browser consistency. Checkboxes are for selecting one or several options in a list, while radios are for selecting one option from many.
Structurally, our
<input>
s and
<label>
s are sibling elements as opposed to an
<input>
within a
<label>
. This is slightly more verbose as you must specify
id
and
for
attributes to relate the
<input>
and
<label>
. We use the sibling selector (
~
) for all our
<input>
states, like
:checked
or
:disabled
. When combined with the
.form-check-label
class, we can easily style the text for each item based on the
<input>
’s state.
Our checks use custom Bootstrap icons to indicate checked or indeterminate states.
Checks
Default checkbox
Checked checkbox
html
<
div
class
=
"
form-check
"
>
<
input
class
=
"
form-check-input
"
type
=
"
checkbox
"
value
=
"
"
id
=
"
checkDefault
"
>
<
label
class
=
"
form-check-label
"
for
=
"
checkDefault
"
>
Default checkbox
</
label
>
</
div
>
<
div
class
=
"
form-check
"
>
<
input
class
=
"
form-check-input
"
type
=
"
checkbox
"
value
=
"
"
id
=
"
checkChecked
"
checked
>
<
label
class
=
"
form-check-label
"
for
=
"
checkChecked
"
>
Checked checkbox
</
label
>
</
div
>
Indeterminate
Checkboxes can utilize the
:indeterminate
pseudo class when manually set via JavaScript (there is no available HTML attribute for specifying it).
Indeterminate checkbox
html
<
div
class
=
"
form-check
"
>
<
input
class
=
"
form-check-input
"
type
=
"
checkbox
"
value
=
"
"
id
=
"
checkIndeterminate
"
>
<
label
class
=
"
form-check-label
"
for
=
"
checkIndeterminate
"
>
Indeterminate checkbox
</
label
>
</
div
>
Disabled
Add the
disabled
attribute and the associated
<label>
s are automatically styled to match with a lighter color to help indicate the input’s state.
Disabled indeterminate checkbox
Disabled checkbox
Disabled checked checkbox
html
<
div
class
=
"
form-check
"
>
<
input
class
=
"
form-check-input
"
type
=
"
checkbox
"
value
=
"
"
id
=
"
checkIndeterminateDisabled
"
disabled
>
<
label
class
=
"
form-check-label
"
for
=
"
checkIndeterminateDisabled
"
>
Disabled indeterminate checkbox
</
label
>
</
div
>
<
div
class
=
"
form-check
"
>
<
input
class
=
"
form-check-input
"
type
=
"
checkbox
"
value
=
"
"
id
=
"
checkDisabled
"
disabled
>
<
label
class
=
"
form-check-label
"
for
=
"
checkDisabled
"
>
Disabled checkbox
</
label
>
</
div
>
<
div
class
=
"
form-check
"
>
<
input
class
=
"
form-check-input
"
type
=
"
checkbox
"
value
=
"
"
id
=
"
checkCheckedDisabled
"
checked
disabled
>
<
label
class
=
"
form-check-label
"
for
=
"
checkCheckedDisabled
"
>
Disabled checked checkbox
</
label
>
</
div
>
Radios
Default radio
Default checked radio
html
<
div
class
=
"
form-check
"
>
<
input
class
=
"
form-check-input
"
type
=
"
radio
"
name
=
"
radioDefault
"
id
=
"
radioDefault1
"
>
<
label
class
=
"
form-check-label
"
for
=
"
radioDefault1
"
>
Default radio
</
label
>
</
div
>
<
div
class
=
"
form-check
"
>
<
input
class
=
"
form-check-input
"
type
=
"
radio
"
name
=
"
radioDefault
"
id
=
"
radioDefault2
"
checked
>
<
label
class
=
"
form-check-label
"
for
=
"
radioDefault2
"
>
Default checked radio
</
label
>
</
div
>
Disabled
Add the
disabled
attribute and the associated
<label>
s are automatically styled to match with a lighter color to help indicate the input’s state.
Disabled radio
Disabled checked radio
html
<
div
class
=
"
form-check
"
>
<
input
class
=
"
form-check-input
"
type
=
"
radio
"
name
=
"
radioDisabled
"
id
=
"
radioDisabled
"
disabled
>
<
label
class
=
"
form-check-label
"
for
=
"
radioDisabled
"
>
Disabled radio
</
label
>
</
div
>
<
div
class
=
"
form-check
"
>
<
input
class
=
"
form-check-input
"
type
=
"
radio
"
name
=
"
radioDisabled
"
id
=
"
radioCheckedDisabled
"
checked
disabled
>
<
label
class
=
"
form-check-label
"
for
=
"
radioCheckedDisabled
"
>
Disabled checked radio
</
label
>
</
div
>
Switches
A switch has the markup of a custom checkbox but uses the
.form-switch
class to render a toggle switch. Consider using
role="switch"
to more accurately convey the nature of the control to assistive technologies that support this role. In older assistive technologies, it will simply be announced as a regular checkbox as a fallback. Switches also support the
disabled
attribute.
Default switch checkbox input
Checked switch checkbox input
Disabled switch checkbox input
Disabled checked switch checkbox input
html
<
div
class
=
"
form-check form-switch
"
>
<
input
class
=
"
form-check-input
"
type
=
"
checkbox
"
role
=
"
switch
"
id
=
"
switchCheckDefault
"
>
<
label
class
=
"
form-check-label
"
for
=
"
switchCheckDefault
"
>
Default switch checkbox input
</
label
>
</
div
>
<
div
class
=
"
form-check form-switch
"
>
<
input
class
=
"
form-check-input
"
type
=
"
checkbox
"
role
=
"
switch
"
id
=
"
switchCheckChecked
"
checked
>
<
label
class
=
"
form-check-label
"
for
=
"
switchCheckChecked
"
>
Checked switch checkbox input
</
label
>
</
div
>
<
div
class
=
"
form-check form-switch
"
>
<
input
class
=
"
form-check-input
"
type
=
"
checkbox
"
role
=
"
switch
"
id
=
"
switchCheckDisabled
"
disabled
>
<
label
class
=
"
form-check-label
"
for
=
"
switchCheckDisabled
"
>
Disabled switch checkbox input
</
label
>
</
div
>
<
div
class
=
"
form-check form-switch
"
>
<
input
class
=
"
form-check-input
"
type
=
"
checkbox
"
role
=
"
switch
"
id
=
"
switchCheckCheckedDisabled
"
checked
disabled
>
<
label
class
=
"
form-check-label
"
for
=
"
switchCheckCheckedDisabled
"
>
Disabled checked switch checkbox input
</
label
>
</
div
>
Native switches
Progressively enhance your switches for mobile Safari (iOS 17.4+) by adding a
switch
attribute to your input to enable haptic feedback when toggling switches, just like native iOS switches. There are no style changes attached to using this attribute in Bootstrap as all our switches use custom styles.
Native switch haptics
html
<
div
class
=
"
form-check form-switch
"
>
<
input
class
=
"
form-check-input
"
type
=
"
checkbox
"
value
=
"
"
id
=
"
checkNativeSwitch
"
switch
>
<
label
class
=
"
form-check-label
"
for
=
"
checkNativeSwitch
"
>
Native switch haptics
</
label
>
</
div
>
Be sure to read more about
the switch attribute on the WebKit blog
. Safari 17.4+ on macOS and iOS both have native-style switches in HTML while other browsers simply fall back to the standard checkbox appearance. Applying the attribute to a non-Bootstrap checkbox in more recent versions of Safari will render a native switch.
Default (stacked)
By default, any number of checkboxes and radios that are immediate sibling will be vertically stacked and appropriately spaced with
.form-check
.
Default checkbox
Disabled checkbox
html
<
div
class
=
"
form-check
"
>
<
input
class
=
"
form-check-input
"
type
=
"
checkbox
"
value
=
"
"
id
=
"
defaultCheck1
"
>
<
label
class
=
"
form-check-label
"
for
=
"
defaultCheck1
"
>
Default checkbox
</
label
>
</
div
>
<
div
class
=
"
form-check
"
>
<
input
class
=
"
form-check-input
"
type
=
"
checkbox
"
value
=
"
"
id
=
"
defaultCheck2
"
disabled
>
<
label
class
=
"
form-check-label
"
for
=
"
defaultCheck2
"
>
Disabled checkbox
</
label
>
</
div
>
Default radio
Second default radio
Disabled radio
html
<
div
class
=
"
form-check
"
>
<
input
class
=
"
form-check-input
"
type
=
"
radio
"
name
=
"
exampleRadios
"
id
=
"
exampleRadios1
"
value
=
"
option1
"
checked
>
<
label
class
=
"
form-check-label
"
for
=
"
exampleRadios1
"
>
Default radio
</
label
>
</
div
>
<
div
class
=
"
form-check
"
>
<
input
class
=
"
form-check-input
"
type
=
"
radio
"
name
=
"
exampleRadios
"
id
=
"
exampleRadios2
"
value
=
"
option2
"
>
<
label
class
=
"
form-check-label
"
for
=
"
exampleRadios2
"
>
Second default radio
</
label
>
</
div
>
<
div
class
=
"
form-check
"
>
<
input
class
=
"
form-check-input
"
type
=
"
radio
"
name
=
"
exampleRadios
"
id
=
"
exampleRadios3
"
value
=
"
option3
"
disabled
>
<
label
class
=
"
form-check-label
"
for
=
"
exampleRadios3
"
>
Disabled radio
</
label
>
</
div
>
Inline
Group checkboxes or radios on the same horizontal row by adding
.form-check-inline
to any
.form-check
.
1
2
3 (disabled)
html
<
div
class
=
"
form-check form-check-inline
"
>
<
input
class
=
"
form-check-input
"
type
=
"
checkbox
"
id
=
"
inlineCheckbox1
"
value
=
"
option1
"
>
<
label
class
=
"
form-check-label
"
for
=
"
inlineCheckbox1
"
>
1
</
label
>
</
div
>
<
div
class
=
"
form-check form-check-inline
"
>
<
input
class
=
"
form-check-input
"
type
=
"
checkbox
"
id
=
"
inlineCheckbox2
"
value
=
"
option2
"
>
<
label
class
=
"
form-check-label
"
for
=
"
inlineCheckbox2
"
>
2
</
label
>
</
div
>
<
div
class
=
"
form-check form-check-inline
"
>
<
input
class
=
"
form-check-input
"
type
=
"
checkbox
"
id
=
"
inlineCheckbox3
"
value
=
"
option3
"
disabled
>
<
label
class
=
"
form-check-label
"
for
=
"
inlineCheckbox3
"
>
3 (disabled)
</
label
>
</
div
>
1
2
3 (disabled)
html
<
div
class
=
"
form-check form-check-inline
"
>
<
input
class
=
"
form-check-input
"
type
=
"
radio
"
name
=
"
inlineRadioOptions
"
id
=
"
inlineRadio1
"
value
=
"
option1
"
>
<
label
class
=
"
form-check-label
"
for
=
"
inlineRadio1
"
>
1
</
label
>
</
div
>
<
div
class
=
"
form-check form-check-inline
"
>
<
input
class
=
"
form-check-input
"
type
=
"
radio
"
name
=
"
inlineRadioOptions
"
id
=
"
inlineRadio2
"
value
=
"
option2
"
>
<
label
class
=
"
form-check-label
"
for
=
"
inlineRadio2
"
>
2
</
label
>
</
div
>
<
div
class
=
"
form-check form-check-inline
"
>
<
input
class
=
"
form-check-input
"
type
=
"
radio
"
name
=
"
inlineRadioOptions
"
id
=
"
inlineRadio3
"
value
=
"
option3
"
disabled
>
<
label
class
=
"
form-check-label
"
for
=
"
inlineRadio3
"
>
3 (disabled)
</
label
>
</
div
>
Reverse
Put your checkboxes, radios, and switches on the opposite side with the
.form-check-reverse
modifier class.
Reverse checkbox
Disabled reverse checkbox
Reverse switch checkbox input
html
<
div
class
=
"
form-check form-check-reverse
"
>
<
input
class
=
"
form-check-input
"
type
=
"
checkbox
"
value
=
"
"
id
=
"
reverseCheck1
"
>
<
label
class
=
"
form-check-label
"
for
=
"
reverseCheck1
"
>
Reverse checkbox
</
label
>
</
div
>
<
div
class
=
"
form-check form-check-reverse
"
>
<
input
class
=
"
form-check-input
"
type
=
"
checkbox
"
value
=
"
"
id
=
"
reverseCheck2
"
disabled
>
<
label
class
=
"
form-check-label
"
for
=
"
reverseCheck2
"
>
Disabled reverse checkbox
</
label
>
</
div
>
<
div
class
=
"
form-check form-switch form-check-reverse
"
>
<
input
class
=
"
form-check-input
"
type
=
"
checkbox
"
id
=
"
switchCheckReverse
"
>
<
label
class
=
"
form-check-label
"
for
=
"
switchCheckReverse
"
>
Reverse switch checkbox input
</
label
>
</
div
>
Without labels
Omit the wrapping
.form-check
for checkboxes and radios that have no label text. Remember to still provide some form of accessible name for assistive technologies (for instance, using
aria-label
). See the
forms overview accessibility
section for details.
html
<
div
>
<
input
class
=
"
form-check-input
"
type
=
"
checkbox
"
id
=
"
checkboxNoLabel
"
value
=
"
"
aria-label
=
"
...
"
>
</
div
>
<
div
>
<
input
class
=
"
form-check-input
"
type
=
"
radio
"
name
=
"
radioNoLabel
"
id
=
"
radioNoLabel1
"
value
=
"
"
aria-label
=
"
...
"
>
</
div
>
Toggle buttons
Create button-like checkboxes and radio buttons by using
.btn
styles rather than
.form-check-label
on the
<label>
elements. These toggle buttons can further be grouped in a
button group
if needed.
Checkbox toggle buttons
Single toggle
Checked
Disabled
html
<
input
type
=
"
checkbox
"
class
=
"
btn-check
"
id
=
"
btn-check
"
autocomplete
=
"
off
"
>
<
label
class
=
"
btn btn-primary
"
for
=
"
btn-check
"
>
Single toggle
</
label
>
<
input
type
=
"
checkbox
"
class
=
"
btn-check
"
id
=
"
btn-check-2
"
checked
autocomplete
=
"
off
"
>
<
label
class
=
"
btn btn-primary
"
for
=
"
btn-check-2
"
>
Checked
</
label
>
<
input
type
=
"
checkbox
"
class
=
"
btn-check
"
id
=
"
btn-check-3
"
autocomplete
=
"
off
"
disabled
>
<
label
class
=
"
btn btn-primary
"
for
=
"
btn-check-3
"
>
Disabled
</
label
>
Single toggle
Checked
Disabled
html
<
input
type
=
"
checkbox
"
class
=
"
btn-check
"
id
=
"
btn-check-4
"
autocomplete
=
"
off
"
>
<
label
class
=
"
btn
"
for
=
"
btn-check-4
"
>
Single toggle
</
label
>
<
input
type
=
"
checkbox
"
class
=
"
btn-check
"
id
=
"
btn-check-5
"
checked
autocomplete
=
"
off
"
>
<
label
class
=
"
btn
"
for
=
"
btn-check-5
"
>
Checked
</
label
>
<
input
type
=
"
checkbox
"
class
=
"
btn-check
"
id
=
"
btn-check-6
"
autocomplete
=
"
off
"
disabled
>
<
label
class
=
"
btn
"
for
=
"
btn-check-6
"
>
Disabled
</
label
>
Visually, these checkbox toggle buttons are identical to the
button plugin toggle buttons
. However, they are conveyed differently by assistive technologies: the checkbox toggles will be announced by screen readers as “checked“/“not checked“ (since, despite their appearance, they are fundamentally still checkboxes), whereas the button plugin toggle buttons will be announced as “button“/“button pressed“. The choice between these two approaches will depend on the type of toggle you are creating, and whether or not the toggle will make sense to users when announced as a checkbox or as an actual button.
Radio toggle buttons
Checked
Radio
Disabled
Radio
html
<
input
type
=
"
radio
"
class
=
"
btn-check
"
name
=
"
options
"
id
=
"
option1
"
autocomplete
=
"
off
"
checked
>
<
label
class
=
"
btn btn-secondary
"
for
=
"
option1
"
>
Checked
</
label
>
<
input
type
=
"
radio
"
class
=
"
btn-check
"
name
=
"
options
"
id
=
"
option2
"
autocomplete
=
"
off
"
>
<
label
class
=
"
btn btn-secondary
"
for
=
"
option2
"
>
Radio
</
label
>
<
input
type
=
"
radio
"
class
=
"
btn-check
"
name
=
"
options
"
id
=
"
option3
"
autocomplete
=
"
off
"
disabled
>
<
label
class
=
"
btn btn-secondary
"
for
=
"
option3
"
>
Disabled
</
label
>
<
input
type
=
"
radio
"
class
=
"
btn-check
"
name
=
"
options
"
id
=
"
option4
"
autocomplete
=
"
off
"
>
<
label
class
=
"
btn btn-secondary
"
for
=
"
option4
"
>
Radio
</
label
>
Checked
Radio
Disabled
Radio
html
<
input
type
=
"
radio
"
class
=
"
btn-check
"
name
=
"
options-base
"
id
=
"
option5
"
autocomplete
=
"
off
"
checked
>
<
label
class
=
"
btn
"
for
=
"
option5
"
>
Checked
</
label
>
<
input
type
=
"
radio
"
class
=
"
btn-check
"
name
=
"
options-base
"
id
=
"
option6
"
autocomplete
=
"
off
"
>
<
label
class
=
"
btn
"
for
=
"
option6
"
>
Radio
</
label
>
<
input
type
=
"
radio
"
class
=
"
btn-check
"
name
=
"
options-base
"
id
=
"
option7
"
autocomplete
=
"
off
"
disabled
>
<
label
class
=
"
btn
"
for
=
"
option7
"
>
Disabled
</
label
>
<
input
type
=
"
radio
"
class
=
"
btn-check
"
name
=
"
options-base
"
id
=
"
option8
"
autocomplete
=
"
off
"
>
<
label
class
=
"
btn
"
for
=
"
option8
"
>
Radio
</
label
>
Outlined styles
Different variants of
.btn
, such as the various outlined styles, are supported.
Single toggle
Checked
Checked success radio
Danger radio
html
<
input
type
=
"
checkbox
"
class
=
"
btn-check
"
id
=
"
btn-check-outlined
"
autocomplete
=
"
off
"
>
<
label
class
=
"
btn btn-outline-primary
"
for
=
"
btn-check-outlined
"
>
Single toggle
</
label
>
<
br
>
<
input
type
=
"
checkbox
"
class
=
"
btn-check
"
id
=
"
btn-check-2-outlined
"
checked
autocomplete
=
"
off
"
>
<
label
class
=
"
btn btn-outline-secondary
"
for
=
"
btn-check-2-outlined
"
>
Checked
</
label
>
<
br
>
<
input
type
=
"
radio
"
class
=
"
btn-check
"
name
=
"
options-outlined
"
id
=
"
success-outlined
"
autocomplete
=
"
off
"
checked
>
<
label
class
=
"
btn btn-outline-success
"
for
=
"
success-outlined
"
>
Checked success radio
</
label
>
<
input
type
=
"
radio
"
class
=
"
btn-check
"
name
=
"
options-outlined
"
id
=
"
danger-outlined
"
autocomplete
=
"
off
"
>
<
label
class
=
"
btn btn-outline-danger
"
for
=
"
danger-outlined
"
>
Danger radio
</
label
>
CSS
Sass variables
Variables for checks:
scss/_variables.scss
$form-check-input-width
:
1em
;
$form-check-min-height
:
$font-size-base
*
$line-height-base
;
$form-check-padding-start
:
$form-check-input-width
+
.5em
;
$form-check-margin-bottom
:
.125rem
;
$form-check-label-color
:
null
;
$form-check-label-cursor
:
null
;
$form-check-transition
:
null
;
$form-check-input-active-filter
:
brightness
(
90%
)
;
$form-check-input-bg
:
$input-bg
;
$form-check-input-border
:
var
(
--
#{$prefix}
border-width
)
solid
var
(
--
#{$prefix}
border-color
)
;
$form-check-input-border-radius
:
.25em
;
$form-check-radio-border-radius
:
50%
;
$form-check-input-focus-border
:
$input-focus-border-color
;
$form-check-input-focus-box-shadow
:
$focus-ring-box-shadow
;
$form-check-input-checked-color
:
$component-active-color
;
$form-check-input-checked-bg-color
:
$component-active-bg
;
$form-check-input-checked-border-color
:
$form-check-input-checked-bg-color
;
$form-check-input-checked-bg-image
:
url
(
"data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'><path fill='none' stroke='#{$form-check-input-checked-color}' stroke-linecap='round' stroke-linejoin='round' stroke-width='3' d='m6 10 3 3 6-6'/></svg>"
)
;
$form-check-radio-checked-bg-image
:
url
(
"data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'><circle r='2' fill='#{$form-check-input-checked-color}'/></svg>"
)
;
$form-check-input-indeterminate-color
:
$component-active-color
;
$form-check-input-indeterminate-bg-color
:
$component-active-bg
;
$form-check-input-indeterminate-border-color
:
$form-check-input-indeterminate-bg-color
;
$form-check-input-indeterminate-bg-image
:
url
(
"data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'><path fill='none' stroke='#{$form-check-input-indeterminate-color}' stroke-linecap='round' stroke-linejoin='round' stroke-width='3' d='M6 10h8'/></svg>"
)
;
$form-check-input-disabled-opacity
:
.5
;
$form-check-label-disabled-opacity
:
$form-check-input-disabled-opacity
;
$form-check-btn-check-disabled-opacity
:
$btn-disabled-opacity
;
$form-check-inline-margin-end
:
1rem
;
Variables for switches:
scss/_variables.scss
$form-switch-color
:
rgba
(
$black
,
.25
)
;
$form-switch-width
:
2em
;
$form-switch-padding-start
:
$form-switch-width
+
.5em
;
$form-switch-bg-image
:
url
(
"data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'><circle r='3' fill='#{$form-switch-color}'/></svg>"
)
;
$form-switch-border-radius
:
$form-switch-width
;
$form-switch-transition
:
background-position .15s ease-in-out
;
$form-switch-focus-color
:
$input-focus-border-color
;
$form-switch-focus-bg-image
:
url
(
"data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'><circle r='3' fill='#{$form-switch-focus-color}'/></svg>"
)
;
$form-switch-checked-color
:
$component-active-color
;
$form-switch-checked-bg-image
:
url
(
"data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'><circle r='3' fill='#{$form-switch-checked-color}'/></svg>"
)
;
$form-switch-checked-bg-position
:
right center
;


## Range · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/forms/range/
- fetched_at: 2026-04-29T13:46:04.390631+00:00

View on GitHub
Range
Use our custom range inputs for consistent cross-browser styling and built-in customization.
On this page
Overview
Create custom
<input type="range">
controls with
.form-range
. The track (the background) and thumb (the value) are both styled to appear the same across browsers. As only Firefox supports “filling” their track from the left or right of the thumb as a means to visually indicate progress, we do not currently support it.
Example range
html
<
label
for
=
"
range1
"
class
=
"
form-label
"
>
Example range
</
label
>
<
input
type
=
"
range
"
class
=
"
form-range
"
id
=
"
range1
"
>
Disabled
Add the
disabled
boolean attribute on an input to give it a grayed out appearance, remove pointer events, and prevent focusing.
Disabled range
html
<
label
for
=
"
disabledRange
"
class
=
"
form-label
"
>
Disabled range
</
label
>
<
input
type
=
"
range
"
class
=
"
form-range
"
id
=
"
disabledRange
"
disabled
>
Min and max
Range inputs have implicit values for
min
and
max
—
0
and
100
, respectively. You may specify new values for those using the
min
and
max
attributes.
Example range
html
<
label
for
=
"
range2
"
class
=
"
form-label
"
>
Example range
</
label
>
<
input
type
=
"
range
"
class
=
"
form-range
"
min
=
"
0
"
max
=
"
5
"
id
=
"
range2
"
>
Steps
By default, range inputs “snap” to integer values. To change this, you can specify a
step
value. In the example below, we double the number of steps by using
step="0.5"
.
Example range
html
<
label
for
=
"
range3
"
class
=
"
form-label
"
>
Example range
</
label
>
<
input
type
=
"
range
"
class
=
"
form-range
"
min
=
"
0
"
max
=
"
5
"
step
=
"
0.5
"
id
=
"
range3
"
>
Output value
The value of the range input can be shown using the
output
element and a bit of JavaScript.
Example range
html
<
label
for
=
"
range4
"
class
=
"
form-label
"
>
Example range
</
label
>
<
input
type
=
"
range
"
class
=
"
form-range
"
min
=
"
0
"
max
=
"
100
"
value
=
"
50
"
id
=
"
range4
"
>
<
output
for
=
"
range4
"
id
=
"
rangeValue
"
aria-hidden
=
"
true
"
>
</
output
>
<
script
>
// This is an example script, please modify as needed
const
rangeInput
=
document
.
getElementById
(
'range4'
)
;
const
rangeOutput
=
document
.
getElementById
(
'rangeValue'
)
;
// Set initial value
rangeOutput
.
textContent
=
rangeInput
.
value
;
rangeInput
.
addEventListener
(
'input'
,
function
(
)
{
rangeOutput
.
textContent
=
this
.
value
;
}
)
;
</
script
>
CSS
Sass variables
scss/_variables.scss
$form-range-track-width
:
100%
;
$form-range-track-height
:
.5rem
;
$form-range-track-cursor
:
pointer
;
$form-range-track-bg
:
var
(
--
#{$prefix}
secondary-bg
)
;
$form-range-track-border-radius
:
1rem
;
$form-range-track-box-shadow
:
var
(
--
#{$prefix}
box-shadow-inset
)
;
$form-range-thumb-width
:
1rem
;
$form-range-thumb-height
:
$form-range-thumb-width
;
$form-range-thumb-bg
:
$component-active-bg
;
$form-range-thumb-border
:
0
;
$form-range-thumb-border-radius
:
1rem
;
$form-range-thumb-box-shadow
:
0 .1rem .25rem
rgba
(
$black
,
.1
)
;
$form-range-thumb-focus-box-shadow
:
0 0 0 1px
$body-bg
,
$input-focus-box-shadow
;
$form-range-thumb-focus-box-shadow-width
:
$input-focus-width
;
// For focus box shadow issue in Edge
$form-range-thumb-active-bg
:
tint-color
(
$component-active-bg
,
70%
)
;
$form-range-thumb-disabled-bg
:
var
(
--
#{$prefix}
secondary-color
)
;
$form-range-thumb-transition
:
background-color .15s ease-in-out
,
border-color .15s ease-in-out
,
box-shadow .15s ease-in-out
;


## Input group · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/forms/input-group/
- fetched_at: 2026-04-29T13:46:04.718140+00:00

View on GitHub
Input group
Easily extend form controls by adding text, buttons, or button groups on either side of textual inputs, custom selects, and custom file inputs.
On this page
Basic example
Place one add-on or button on either side of an input. You may also place one on both sides of an input. Remember to place
<label>
s outside the input group.
@
@example.com
Your vanity URL
https://example.com/users/
Example help text goes outside the input group.
$
.00
@
With textarea
html
<
div
class
=
"
input-group mb-3
"
>
<
span
class
=
"
input-group-text
"
id
=
"
basic-addon1
"
>
@
</
span
>
<
input
type
=
"
text
"
class
=
"
form-control
"
placeholder
=
"
Username
"
aria-label
=
"
Username
"
aria-describedby
=
"
basic-addon1
"
>
</
div
>
<
div
class
=
"
input-group mb-3
"
>
<
input
type
=
"
text
"
class
=
"
form-control
"
placeholder
=
"
Recipient’s username
"
aria-label
=
"
Recipient’s username
"
aria-describedby
=
"
basic-addon2
"
>
<
span
class
=
"
input-group-text
"
id
=
"
basic-addon2
"
>
@example.com
</
span
>
</
div
>
<
div
class
=
"
mb-3
"
>
<
label
for
=
"
basic-url
"
class
=
"
form-label
"
>
Your vanity URL
</
label
>
<
div
class
=
"
input-group
"
>
<
span
class
=
"
input-group-text
"
id
=
"
basic-addon3
"
>
https://example.com/users/
</
span
>
<
input
type
=
"
text
"
class
=
"
form-control
"
id
=
"
basic-url
"
aria-describedby
=
"
basic-addon3 basic-addon4
"
>
</
div
>
<
div
class
=
"
form-text
"
id
=
"
basic-addon4
"
>
Example help text goes outside the input group.
</
div
>
</
div
>
<
div
class
=
"
input-group mb-3
"
>
<
span
class
=
"
input-group-text
"
>
$
</
span
>
<
input
type
=
"
text
"
class
=
"
form-control
"
aria-label
=
"
Amount (to the nearest dollar)
"
>
<
span
class
=
"
input-group-text
"
>
.00
</
span
>
</
div
>
<
div
class
=
"
input-group mb-3
"
>
<
input
type
=
"
text
"
class
=
"
form-control
"
placeholder
=
"
Username
"
aria-label
=
"
Username
"
>
<
span
class
=
"
input-group-text
"
>
@
</
span
>
<
input
type
=
"
text
"
class
=
"
form-control
"
placeholder
=
"
Server
"
aria-label
=
"
Server
"
>
</
div
>
<
div
class
=
"
input-group
"
>
<
span
class
=
"
input-group-text
"
>
With textarea
</
span
>
<
textarea
class
=
"
form-control
"
aria-label
=
"
With textarea
"
>
</
textarea
>
</
div
>
Wrapping
Input groups wrap by default via
flex-wrap: wrap
in order to accommodate custom form field validation within an input group. You may disable this with
.flex-nowrap
.
@
html
<
div
class
=
"
input-group flex-nowrap
"
>
<
span
class
=
"
input-group-text
"
id
=
"
addon-wrapping
"
>
@
</
span
>
<
input
type
=
"
text
"
class
=
"
form-control
"
placeholder
=
"
Username
"
aria-label
=
"
Username
"
aria-describedby
=
"
addon-wrapping
"
>
</
div
>
Border radius
Due to limitations of browser support at the time,
border-radius
styles can only be applied to the first and last children within the
.input-group
class. Any non-visible element in one of those positions will cause the input group to render incorrectly. This will unfortunately not be fixed until v6 most likely.
@
html
<
div
class
=
"
input-group
"
>
<
span
class
=
"
input-group-text
"
id
=
"
visible-addon
"
>
@
</
span
>
<
input
type
=
"
text
"
class
=
"
form-control
"
placeholder
=
"
Username
"
aria-label
=
"
Username
"
aria-describedby
=
"
visible-addon
"
>
<
input
type
=
"
text
"
class
=
"
form-control d-none
"
placeholder
=
"
Hidden input
"
aria-label
=
"
Hidden input
"
aria-describedby
=
"
visible-addon
"
>
</
div
>
Sizing
Add the relative form sizing classes to the
.input-group
itself and contents within will automatically resize—no need for repeating the form control size classes on each element.
Sizing on the individual input group elements isn’t supported.
Small
Default
Large
html
<
div
class
=
"
input-group input-group-sm mb-3
"
>
<
span
class
=
"
input-group-text
"
id
=
"
inputGroup-sizing-sm
"
>
Small
</
span
>
<
input
type
=
"
text
"
class
=
"
form-control
"
aria-label
=
"
Sizing example input
"
aria-describedby
=
"
inputGroup-sizing-sm
"
>
</
div
>
<
div
class
=
"
input-group mb-3
"
>
<
span
class
=
"
input-group-text
"
id
=
"
inputGroup-sizing-default
"
>
Default
</
span
>
<
input
type
=
"
text
"
class
=
"
form-control
"
aria-label
=
"
Sizing example input
"
aria-describedby
=
"
inputGroup-sizing-default
"
>
</
div
>
<
div
class
=
"
input-group input-group-lg
"
>
<
span
class
=
"
input-group-text
"
id
=
"
inputGroup-sizing-lg
"
>
Large
</
span
>
<
input
type
=
"
text
"
class
=
"
form-control
"
aria-label
=
"
Sizing example input
"
aria-describedby
=
"
inputGroup-sizing-lg
"
>
</
div
>
Checkboxes and radios
Place any checkbox or radio option within an input group’s addon instead of text. We recommend adding
.mt-0
to the
.form-check-input
when there’s no visible text next to the input.
html
<
div
class
=
"
input-group mb-3
"
>
<
div
class
=
"
input-group-text
"
>
<
input
class
=
"
form-check-input mt-0
"
type
=
"
checkbox
"
value
=
"
"
aria-label
=
"
Checkbox for following text input
"
>
</
div
>
<
input
type
=
"
text
"
class
=
"
form-control
"
aria-label
=
"
Text input with checkbox
"
>
</
div
>
<
div
class
=
"
input-group
"
>
<
div
class
=
"
input-group-text
"
>
<
input
class
=
"
form-check-input mt-0
"
type
=
"
radio
"
value
=
"
"
aria-label
=
"
Radio button for following text input
"
>
</
div
>
<
input
type
=
"
text
"
class
=
"
form-control
"
aria-label
=
"
Text input with radio button
"
>
</
div
>
Multiple inputs
While multiple
<input>
s are supported visually, validation styles are only available for input groups with a single
<input>
.
First and last name
html
<
div
class
=
"
input-group
"
>
<
span
class
=
"
input-group-text
"
>
First and last name
</
span
>
<
input
type
=
"
text
"
aria-label
=
"
First name
"
class
=
"
form-control
"
>
<
input
type
=
"
text
"
aria-label
=
"
Last name
"
class
=
"
form-control
"
>
</
div
>
Multiple addons
Multiple add-ons are supported and can be mixed with checkbox and radio input versions.
$
0.00
$
0.00
html
<
div
class
=
"
input-group mb-3
"
>
<
span
class
=
"
input-group-text
"
>
$
</
span
>
<
span
class
=
"
input-group-text
"
>
0.00
</
span
>
<
input
type
=
"
text
"
class
=
"
form-control
"
aria-label
=
"
Dollar amount (with dot and two decimal places)
"
>
</
div
>
<
div
class
=
"
input-group
"
>
<
input
type
=
"
text
"
class
=
"
form-control
"
aria-label
=
"
Dollar amount (with dot and two decimal places)
"
>
<
span
class
=
"
input-group-text
"
>
$
</
span
>
<
span
class
=
"
input-group-text
"
>
0.00
</
span
>
</
div
>
Button addons
html
<
div
class
=
"
input-group mb-3
"
>
<
button
class
=
"
btn btn-outline-secondary
"
type
=
"
button
"
id
=
"
button-addon1
"
>
Button
</
button
>
<
input
type
=
"
text
"
class
=
"
form-control
"
placeholder
=
"
"
aria-label
=
"
Example text with button addon
"
aria-describedby
=
"
button-addon1
"
>
</
div
>
<
div
class
=
"
input-group mb-3
"
>
<
input
type
=
"
text
"
class
=
"
form-control
"
placeholder
=
"
Recipient’s username
"
aria-label
=
"
Recipient’s username
"
aria-describedby
=
"
button-addon2
"
>
<
button
class
=
"
btn btn-outline-secondary
"
type
=
"
button
"
id
=
"
button-addon2
"
>
Button
</
button
>
</
div
>
<
div
class
=
"
input-group mb-3
"
>
<
button
class
=
"
btn btn-outline-secondary
"
type
=
"
button
"
>
Button
</
button
>
<
button
class
=
"
btn btn-outline-secondary
"
type
=
"
button
"
>
Button
</
button
>
<
input
type
=
"
text
"
class
=
"
form-control
"
placeholder
=
"
"
aria-label
=
"
Example text with two button addons
"
>
</
div
>
<
div
class
=
"
input-group
"
>
<
input
type
=
"
text
"
class
=
"
form-control
"
placeholder
=
"
Recipient’s username
"
aria-label
=
"
Recipient’s username with two button addons
"
>
<
button
class
=
"
btn btn-outline-secondary
"
type
=
"
button
"
>
Button
</
button
>
<
button
class
=
"
btn btn-outline-secondary
"
type
=
"
button
"
>
Button
</
button
>
</
div
>
Buttons with dropdowns
Action
Another action
Something else here
Separated link
Action
Another action
Something else here
Separated link
Action before
Another action before
Something else here
Separated link
Action
Another action
Something else here
Separated link
html
<
div
class
=
"
input-group mb-3
"
>
<
button
class
=
"
btn btn-outline-secondary dropdown-toggle
"
type
=
"
button
"
data-bs-toggle
=
"
dropdown
"
aria-expanded
=
"
false
"
>
Dropdown
</
button
>
<
ul
class
=
"
dropdown-menu
"
>
<
li
>
<
a
class
=
"
dropdown-item
"
href
=
"
#
"
>
Action
</
a
>
</
li
>
<
li
>
<
a
class
=
"
dropdown-item
"
href
=
"
#
"
>
Another action
</
a
>
</
li
>
<
li
>
<
a
class
=
"
dropdown-item
"
href
=
"
#
"
>
Something else here
</
a
>
</
li
>
<
li
>
<
hr
class
=
"
dropdown-divider
"
>
</
li
>
<
li
>
<
a
class
=
"
dropdown-item
"
href
=
"
#
"
>
Separated link
</
a
>
</
li
>
</
ul
>
<
input
type
=
"
text
"
class
=
"
form-control
"
aria-label
=
"
Text input with dropdown button
"
>
</
div
>
<
div
class
=
"
input-group mb-3
"
>
<
input
type
=
"
text
"
class
=
"
form-control
"
aria-label
=
"
Text input with dropdown button
"
>
<
button
class
=
"
btn btn-outline-secondary dropdown-toggle
"
type
=
"
button
"
data-bs-toggle
=
"
dropdown
"
aria-expanded
=
"
false
"
>
Dropdown
</
button
>
<
ul
class
=
"
dropdown-menu dropdown-menu-end
"
>
<
li
>
<
a
class
=
"
dropdown-item
"
href
=
"
#
"
>
Action
</
a
>
</
li
>
<
li
>
<
a
class
=
"
dropdown-item
"
href
=
"
#
"
>
Another action
</
a
>
</
li
>
<
li
>
<
a
class
=
"
dropdown-item
"
href
=
"
#
"
>
Something else here
</
a
>
</
li
>
<
li
>
<
hr
class
=
"
dropdown-divider
"
>
</
li
>
<
li
>
<
a
class
=
"
dropdown-item
"
href
=
"
#
"
>
Separated link
</
a
>
</
li
>
</
ul
>
</
div
>
<
div
class
=
"
input-group
"
>
<
button
class
=
"
btn btn-outline-secondary dropdown-toggle
"
type
=
"
button
"
data-bs-toggle
=
"
dropdown
"
aria-expanded
=
"
false
"
>
Dropdown
</
button
>
<
ul
class
=
"
dropdown-menu
"
>
<
li
>
<
a
class
=
"
dropdown-item
"
href
=
"
#
"
>
Action before
</
a
>
</
li
>
<
li
>
<
a
class
=
"
dropdown-item
"
href
=
"
#
"
>
Another action before
</
a
>
</
li
>
<
li
>
<
a
class
=
"
dropdown-item
"
href
=
"
#
"
>
Something else here
</
a
>
</
li
>
<
li
>
<
hr
class
=
"
dropdown-divider
"
>
</
li
>
<
li
>
<
a
class
=
"
dropdown-item
"
href
=
"
#
"
>
Separated link
</
a
>
</
li
>
</
ul
>
<
input
type
=
"
text
"
class
=
"
form-control
"
aria-label
=
"
Text input with 2 dropdown buttons
"
>
<
button
class
=
"
btn btn-outline-secondary dropdown-toggle
"
type
=
"
button
"
data-bs-toggle
=
"
dropdown
"
aria-expanded
=
"
false
"
>
Dropdown
</
button
>
<
ul
class
=
"
dropdown-menu dropdown-menu-end
"
>
<
li
>
<
a
class
=
"
dropdown-item
"
href
=
"
#
"
>
Action
</
a
>
</
li
>
<
li
>
<
a
class
=
"
dropdown-item
"
href
=
"
#
"
>
Another action
</
a
>
</
li
>
<
li
>
<
a
class
=
"
dropdown-item
"
href
=
"
#
"
>
Something else here
</
a
>
</
li
>
<
li
>
<
hr
class
=
"
dropdown-divider
"
>
</
li
>
<
li
>
<
a
class
=
"
dropdown-item
"
href
=
"
#
"
>
Separated link
</
a
>
</
li
>
</
ul
>
</
div
>
Segmented buttons
Action
Another action
Something else here
Separated link
Action
Another action
Something else here
Separated link
html
<
div
class
=
"
input-group mb-3
"
>
<
button
type
=
"
button
"
class
=
"
btn btn-outline-secondary
"
>
Action
</
button
>
<
button
type
=
"
button
"
class
=
"
btn btn-outline-secondary dropdown-toggle dropdown-toggle-split
"
data-bs-toggle
=
"
dropdown
"
aria-expanded
=
"
false
"
>
<
span
class
=
"
visually-hidden
"
>
Toggle Dropdown
</
span
>
</
button
>
<
ul
class
=
"
dropdown-menu
"
>
<
li
>
<
a
class
=
"
dropdown-item
"
href
=
"
#
"
>
Action
</
a
>
</
li
>
<
li
>
<
a
class
=
"
dropdown-item
"
href
=
"
#
"
>
Another action
</
a
>
</
li
>
<
li
>
<
a
class
=
"
dropdown-item
"
href
=
"
#
"
>
Something else here
</
a
>
</
li
>
<
li
>
<
hr
class
=
"
dropdown-divider
"
>
</
li
>
<
li
>
<
a
class
=
"
dropdown-item
"
href
=
"
#
"
>
Separated link
</
a
>
</
li
>
</
ul
>
<
input
type
=
"
text
"
class
=
"
form-control
"
aria-label
=
"
Text input with segmented dropdown button
"
>
</
div
>
<
div
class
=
"
input-group
"
>
<
input
type
=
"
text
"
class
=
"
form-control
"
aria-label
=
"
Text input with segmented dropdown button
"
>
<
button
type
=
"
button
"
class
=
"
btn btn-outline-secondary
"
>
Action
</
button
>
<
button
type
=
"
button
"
class
=
"
btn btn-outline-secondary dropdown-toggle dropdown-toggle-split
"
data-bs-toggle
=
"
dropdown
"
aria-expanded
=
"
false
"
>
<
span
class
=
"
visually-hidden
"
>
Toggle Dropdown
</
span
>
</
button
>
<
ul
class
=
"
dropdown-menu dropdown-menu-end
"
>
<
li
>
<
a
class
=
"
dropdown-item
"
href
=
"
#
"
>
Action
</
a
>
</
li
>
<
li
>
<
a
class
=
"
dropdown-item
"
href
=
"
#
"
>
Another action
</
a
>
</
li
>
<
li
>
<
a
class
=
"
dropdown-item
"
href
=
"
#
"
>
Something else here
</
a
>
</
li
>
<
li
>
<
hr
class
=
"
dropdown-divider
"
>
</
li
>
<
li
>
<
a
class
=
"
dropdown-item
"
href
=
"
#
"
>
Separated link
</
a
>
</
li
>
</
ul
>
</
div
>
Custom forms
Input groups include support for custom selects and custom file inputs. Browser default versions of these are not supported.
Custom select
Options
Choose...
One
Two
Three
Choose...
One
Two
Three
Options
Choose...
One
Two
Three
Choose...
One
Two
Three
html
<
div
class
=
"
input-group mb-3
"
>
<
label
class
=
"
input-group-text
"
for
=
"
inputGroupSelect01
"
>
Options
</
label
>
<
select
class
=
"
form-select
"
id
=
"
inputGroupSelect01
"
>
<
option
selected
>
Choose...
</
option
>
<
option
value
=
"
1
"
>
One
</
option
>
<
option
value
=
"
2
"
>
Two
</
option
>
<
option
value
=
"
3
"
>
Three
</
option
>
</
select
>
</
div
>
<
div
class
=
"
input-group mb-3
"
>
<
select
class
=
"
form-select
"
id
=
"
inputGroupSelect02
"
>
<
option
selected
>
Choose...
</
option
>
<
option
value
=
"
1
"
>
One
</
option
>
<
option
value
=
"
2
"
>
Two
</
option
>
<
option
value
=
"
3
"
>
Three
</
option
>
</
select
>
<
label
class
=
"
input-group-text
"
for
=
"
inputGroupSelect02
"
>
Options
</
label
>
</
div
>
<
div
class
=
"
input-group mb-3
"
>
<
button
class
=
"
btn btn-outline-secondary
"
type
=
"
button
"
>
Button
</
button
>
<
select
class
=
"
form-select
"
id
=
"
inputGroupSelect03
"
aria-label
=
"
Example select with button addon
"
>
<
option
selected
>
Choose...
</
option
>
<
option
value
=
"
1
"
>
One
</
option
>
<
option
value
=
"
2
"
>
Two
</
option
>
<
option
value
=
"
3
"
>
Three
</
option
>
</
select
>
</
div
>
<
div
class
=
"
input-group
"
>
<
select
class
=
"
form-select
"
id
=
"
inputGroupSelect04
"
aria-label
=
"
Example select with button addon
"
>
<
option
selected
>
Choose...
</
option
>
<
option
value
=
"
1
"
>
One
</
option
>
<
option
value
=
"
2
"
>
Two
</
option
>
<
option
value
=
"
3
"
>
Three
</
option
>
</
select
>
<
button
class
=
"
btn btn-outline-secondary
"
type
=
"
button
"
>
Button
</
button
>
</
div
>
Custom file input
Upload
Upload
html
<
div
class
=
"
input-group mb-3
"
>
<
label
class
=
"
input-group-text
"
for
=
"
inputGroupFile01
"
>
Upload
</
label
>
<
input
type
=
"
file
"
class
=
"
form-control
"
id
=
"
inputGroupFile01
"
>
</
div
>
<
div
class
=
"
input-group mb-3
"
>
<
input
type
=
"
file
"
class
=
"
form-control
"
id
=
"
inputGroupFile02
"
>
<
label
class
=
"
input-group-text
"
for
=
"
inputGroupFile02
"
>
Upload
</
label
>
</
div
>
<
div
class
=
"
input-group mb-3
"
>
<
button
class
=
"
btn btn-outline-secondary
"
type
=
"
button
"
id
=
"
inputGroupFileAddon03
"
>
Button
</
button
>
<
input
type
=
"
file
"
class
=
"
form-control
"
id
=
"
inputGroupFile03
"
aria-describedby
=
"
inputGroupFileAddon03
"
aria-label
=
"
Upload
"
>
</
div
>
<
div
class
=
"
input-group
"
>
<
input
type
=
"
file
"
class
=
"
form-control
"
id
=
"
inputGroupFile04
"
aria-describedby
=
"
inputGroupFileAddon04
"
aria-label
=
"
Upload
"
>
<
button
class
=
"
btn btn-outline-secondary
"
type
=
"
button
"
id
=
"
inputGroupFileAddon04
"
>
Button
</
button
>
</
div
>
CSS
Sass variables
scss/_variables.scss
$input-group-addon-padding-y
:
$input-padding-y
;
$input-group-addon-padding-x
:
$input-padding-x
;
$input-group-addon-font-weight
:
$input-font-weight
;
$input-group-addon-color
:
$input-color
;
$input-group-addon-bg
:
var
(
--
#{$prefix}
tertiary-bg
)
;
$input-group-addon-border-color
:
$input-border-color
;


## Floating labels · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/forms/floating-labels/
- fetched_at: 2026-04-29T13:46:05.128660+00:00

View on GitHub
Floating labels
Create beautifully simple form labels that float over your input fields.
On this page
Example
Wrap a pair of
<input class="form-control">
and
<label>
elements in
.form-floating
to enable floating labels with Bootstrap’s textual form fields.
A non-empty
placeholder
attribute is required on each
<input>
as our CSS-only floating label implementation relies on the
:placeholder-shown
pseudo-element to detect when the input is empty. The placeholder text itself is not visible; only the
<label>
is shown to users.
Also note that the
<input>
must come first so we can utilize a sibling selector (i.e.,
~
).
Email address
Password
html
<
div
class
=
"
form-floating mb-3
"
>
<
input
type
=
"
email
"
class
=
"
form-control
"
id
=
"
floatingInput
"
placeholder
=
"
name@example.com
"
>
<
label
for
=
"
floatingInput
"
>
Email address
</
label
>
</
div
>
<
div
class
=
"
form-floating
"
>
<
input
type
=
"
password
"
class
=
"
form-control
"
id
=
"
floatingPassword
"
placeholder
=
"
Password
"
>
<
label
for
=
"
floatingPassword
"
>
Password
</
label
>
</
div
>
When there’s a
value
already defined,
<label>
s will automatically adjust to their floated position.
html
<
form
class
=
"
form-floating
"
>
<
input
type
=
"
email
"
class
=
"
form-control
"
id
=
"
floatingInputValue
"
placeholder
=
"
name@example.com
"
value
=
"
test@example.com
"
>
<
label
for
=
"
floatingInputValue
"
>
Input with value
</
label
>
</
form
>
Form validation styles also work as expected.
html
<
form
class
=
"
form-floating
"
>
<
input
type
=
"
email
"
class
=
"
form-control is-invalid
"
id
=
"
floatingInputInvalid
"
placeholder
=
"
name@example.com
"
value
=
"
test@example.com
"
>
<
label
for
=
"
floatingInputInvalid
"
>
Invalid input
</
label
>
</
form
>
Textareas
By default,
<textarea>
s with
.form-control
will be the same height as
<input>
s.
Comments
html
<
div
class
=
"
form-floating
"
>
<
textarea
class
=
"
form-control
"
placeholder
=
"
Leave a comment here
"
id
=
"
floatingTextarea
"
>
</
textarea
>
<
label
for
=
"
floatingTextarea
"
>
Comments
</
label
>
</
div
>
To set a custom height on your
<textarea>
, do not use the
rows
attribute. Instead, set an explicit
height
(either inline or via custom CSS).
Comments
html
<
div
class
=
"
form-floating
"
>
<
textarea
class
=
"
form-control
"
placeholder
=
"
Leave a comment here
"
id
=
"
floatingTextarea2
"
style
=
"
height
:
100px
"
>
</
textarea
>
<
label
for
=
"
floatingTextarea2
"
>
Comments
</
label
>
</
div
>
Selects
Other than
.form-control
, floating labels are only available on
.form-select
s. They work in the same way, but unlike
<input>
s, they’ll always show the
<label>
in its floated state.
Selects with
size
and
multiple
are not supported.
Open this select menu
One
Two
Three
Works with selects
html
<
div
class
=
"
form-floating
"
>
<
select
class
=
"
form-select
"
id
=
"
floatingSelect
"
aria-label
=
"
Floating label select example
"
>
<
option
selected
>
Open this select menu
</
option
>
<
option
value
=
"
1
"
>
One
</
option
>
<
option
value
=
"
2
"
>
Two
</
option
>
<
option
value
=
"
3
"
>
Three
</
option
>
</
select
>
<
label
for
=
"
floatingSelect
"
>
Works with selects
</
label
>
</
div
>
Disabled
Add the
disabled
boolean attribute on an input, a textarea or a select to give it a grayed out appearance, remove pointer events, and prevent focusing.
Email address
Comments
Disabled textarea with some text inside
Comments
Open this select menu
One
Two
Three
Works with selects
html
<
div
class
=
"
form-floating mb-3
"
>
<
input
type
=
"
email
"
class
=
"
form-control
"
id
=
"
floatingInputDisabled
"
placeholder
=
"
name@example.com
"
disabled
>
<
label
for
=
"
floatingInputDisabled
"
>
Email address
</
label
>
</
div
>
<
div
class
=
"
form-floating mb-3
"
>
<
textarea
class
=
"
form-control
"
placeholder
=
"
Leave a comment here
"
id
=
"
floatingTextareaDisabled
"
disabled
>
</
textarea
>
<
label
for
=
"
floatingTextareaDisabled
"
>
Comments
</
label
>
</
div
>
<
div
class
=
"
form-floating mb-3
"
>
<
textarea
class
=
"
form-control
"
placeholder
=
"
Leave a comment here
"
id
=
"
floatingTextarea2Disabled
"
style
=
"
height
:
100px
"
disabled
>
Disabled textarea with some text inside
</
textarea
>
<
label
for
=
"
floatingTextarea2Disabled
"
>
Comments
</
label
>
</
div
>
<
div
class
=
"
form-floating
"
>
<
select
class
=
"
form-select
"
id
=
"
floatingSelectDisabled
"
aria-label
=
"
Floating label disabled select example
"
disabled
>
<
option
selected
>
Open this select menu
</
option
>
<
option
value
=
"
1
"
>
One
</
option
>
<
option
value
=
"
2
"
>
Two
</
option
>
<
option
value
=
"
3
"
>
Three
</
option
>
</
select
>
<
label
for
=
"
floatingSelectDisabled
"
>
Works with selects
</
label
>
</
div
>
Readonly plaintext
Floating labels also support
.form-control-plaintext
, which can be helpful for toggling from an editable
<input>
to a plaintext value without affecting the page layout.
Empty input
Input with value
html
<
div
class
=
"
form-floating mb-3
"
>
<
input
type
=
"
email
"
readonly
class
=
"
form-control-plaintext
"
id
=
"
floatingEmptyPlaintextInput
"
placeholder
=
"
name@example.com
"
>
<
label
for
=
"
floatingEmptyPlaintextInput
"
>
Empty input
</
label
>
</
div
>
<
div
class
=
"
form-floating mb-3
"
>
<
input
type
=
"
email
"
readonly
class
=
"
form-control-plaintext
"
id
=
"
floatingPlaintextInput
"
placeholder
=
"
name@example.com
"
value
=
"
name@example.com
"
>
<
label
for
=
"
floatingPlaintextInput
"
>
Input with value
</
label
>
</
div
>
Input groups
Floating labels also support
.input-group
.
@
Username
html
<
div
class
=
"
input-group mb-3
"
>
<
span
class
=
"
input-group-text
"
>
@
</
span
>
<
div
class
=
"
form-floating
"
>
<
input
type
=
"
text
"
class
=
"
form-control
"
id
=
"
floatingInputGroup1
"
placeholder
=
"
Username
"
>
<
label
for
=
"
floatingInputGroup1
"
>
Username
</
label
>
</
div
>
</
div
>
When using
.input-group
and
.form-floating
along with form validation, the
-feedback
should be placed outside of the
.form-floating
, but inside of the
.input-group
. This means that the feedback will need to be shown using javascript.
@
Username
Please choose a username.
html
<
div
class
=
"
input-group has-validation
"
>
<
span
class
=
"
input-group-text
"
>
@
</
span
>
<
div
class
=
"
form-floating is-invalid
"
>
<
input
type
=
"
text
"
class
=
"
form-control is-invalid
"
id
=
"
floatingInputGroup2
"
placeholder
=
"
Username
"
required
>
<
label
for
=
"
floatingInputGroup2
"
>
Username
</
label
>
</
div
>
<
div
class
=
"
invalid-feedback
"
>
Please choose a username.
</
div
>
</
div
>
Layout
When working with the Bootstrap grid system, be sure to place form elements within column classes.
Email address
Open this select menu
One
Two
Three
Works with selects
html
<
div
class
=
"
row g-2
"
>
<
div
class
=
"
col-md
"
>
<
div
class
=
"
form-floating
"
>
<
input
type
=
"
email
"
class
=
"
form-control
"
id
=
"
floatingInputGrid
"
placeholder
=
"
name@example.com
"
value
=
"
mdo@example.com
"
>
<
label
for
=
"
floatingInputGrid
"
>
Email address
</
label
>
</
div
>
</
div
>
<
div
class
=
"
col-md
"
>
<
div
class
=
"
form-floating
"
>
<
select
class
=
"
form-select
"
id
=
"
floatingSelectGrid
"
>
<
option
selected
>
Open this select menu
</
option
>
<
option
value
=
"
1
"
>
One
</
option
>
<
option
value
=
"
2
"
>
Two
</
option
>
<
option
value
=
"
3
"
>
Three
</
option
>
</
select
>
<
label
for
=
"
floatingSelectGrid
"
>
Works with selects
</
label
>
</
div
>
</
div
>
</
div
>
CSS
Sass variables
scss/_variables.scss
$form-floating-height
:
add
(
3.5rem
,
$input-height-border
)
;
$form-floating-line-height
:
1.25
;
$form-floating-padding-x
:
$input-padding-x
;
$form-floating-padding-y
:
1rem
;
$form-floating-input-padding-t
:
1.625rem
;
$form-floating-input-padding-b
:
.625rem
;
$form-floating-label-height
:
1.5em
;
$form-floating-label-opacity
:
.65
;
$form-floating-label-transform
:
scale
(
.85
)
translateY
(
-.5rem
)
translateX
(
.15rem
)
;
$form-floating-label-disabled-color
:
$gray-600
;
$form-floating-transition
:
opacity .1s ease-in-out
,
transform .1s ease-in-out
;


## Layout · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/forms/layout/
- fetched_at: 2026-04-29T13:46:05.624244+00:00

View on GitHub
Layout
Give your forms some structure—from inline to horizontal to custom grid implementations—with our form layout options.
On this page
Forms
Every group of form fields should reside in a
<form>
element. Bootstrap provides no default styling for the
<form>
element, but there are some powerful browser features that are provided by default.
New to browser forms? Consider reviewing
the MDN form docs
for an overview and complete list of available attributes.
<button>
s within a
<form>
default to
type="submit"
, so strive to be specific and always include a
type
.
Since Bootstrap applies
display: block
and
width: 100%
to almost all our form controls, forms will by default stack vertically. Additional classes can be used to vary this layout on a per-form basis.
Utilities
Margin utilities
are the easiest way to add some structure to forms. They provide basic grouping of labels, controls, optional form text, and form validation messaging. We recommend sticking to
margin-bottom
utilities, and using a single direction throughout the form for consistency.
Feel free to build your forms however you like, with
<fieldset>
s,
<div>
s, or nearly any other element.
Example label
Another label
html
<
div
class
=
"
mb-3
"
>
<
label
for
=
"
formGroupExampleInput
"
class
=
"
form-label
"
>
Example label
</
label
>
<
input
type
=
"
text
"
class
=
"
form-control
"
id
=
"
formGroupExampleInput
"
placeholder
=
"
Example input placeholder
"
>
</
div
>
<
div
class
=
"
mb-3
"
>
<
label
for
=
"
formGroupExampleInput2
"
class
=
"
form-label
"
>
Another label
</
label
>
<
input
type
=
"
text
"
class
=
"
form-control
"
id
=
"
formGroupExampleInput2
"
placeholder
=
"
Another input placeholder
"
>
</
div
>
Form grid
More complex forms can be built using our grid classes. Use these for form layouts that require multiple columns, varied widths, and additional alignment options.
Requires the
$enable-grid-classes
Sass variable to be enabled
(on by default).
html
<
div
class
=
"
row
"
>
<
div
class
=
"
col
"
>
<
input
type
=
"
text
"
class
=
"
form-control
"
placeholder
=
"
First name
"
aria-label
=
"
First name
"
>
</
div
>
<
div
class
=
"
col
"
>
<
input
type
=
"
text
"
class
=
"
form-control
"
placeholder
=
"
Last name
"
aria-label
=
"
Last name
"
>
</
div
>
</
div
>
Gutters
By adding
gutter modifier classes
, you can have control over the gutter width in as well the inline as block direction.
Also requires the
$enable-grid-classes
Sass variable to be enabled
(on by default).
html
<
div
class
=
"
row g-3
"
>
<
div
class
=
"
col
"
>
<
input
type
=
"
text
"
class
=
"
form-control
"
placeholder
=
"
First name
"
aria-label
=
"
First name
"
>
</
div
>
<
div
class
=
"
col
"
>
<
input
type
=
"
text
"
class
=
"
form-control
"
placeholder
=
"
Last name
"
aria-label
=
"
Last name
"
>
</
div
>
</
div
>
More complex layouts can also be created with the grid system.
html
<
form
class
=
"
row g-3
"
>
<
div
class
=
"
col-md-6
"
>
<
label
for
=
"
inputEmail4
"
class
=
"
form-label
"
>
Email
</
label
>
<
input
type
=
"
email
"
class
=
"
form-control
"
id
=
"
inputEmail4
"
>
</
div
>
<
div
class
=
"
col-md-6
"
>
<
label
for
=
"
inputPassword4
"
class
=
"
form-label
"
>
Password
</
label
>
<
input
type
=
"
password
"
class
=
"
form-control
"
id
=
"
inputPassword4
"
>
</
div
>
<
div
class
=
"
col-12
"
>
<
label
for
=
"
inputAddress
"
class
=
"
form-label
"
>
Address
</
label
>
<
input
type
=
"
text
"
class
=
"
form-control
"
id
=
"
inputAddress
"
placeholder
=
"
1234 Main St
"
>
</
div
>
<
div
class
=
"
col-12
"
>
<
label
for
=
"
inputAddress2
"
class
=
"
form-label
"
>
Address 2
</
label
>
<
input
type
=
"
text
"
class
=
"
form-control
"
id
=
"
inputAddress2
"
placeholder
=
"
Apartment, studio, or floor
"
>
</
div
>
<
div
class
=
"
col-md-6
"
>
<
label
for
=
"
inputCity
"
class
=
"
form-label
"
>
City
</
label
>
<
input
type
=
"
text
"
class
=
"
form-control
"
id
=
"
inputCity
"
>
</
div
>
<
div
class
=
"
col-md-4
"
>
<
label
for
=
"
inputState
"
class
=
"
form-label
"
>
State
</
label
>
<
select
id
=
"
inputState
"
class
=
"
form-select
"
>
<
option
selected
>
Choose...
</
option
>
<
option
>
...
</
option
>
</
select
>
</
div
>
<
div
class
=
"
col-md-2
"
>
<
label
for
=
"
inputZip
"
class
=
"
form-label
"
>
Zip
</
label
>
<
input
type
=
"
text
"
class
=
"
form-control
"
id
=
"
inputZip
"
>
</
div
>
<
div
class
=
"
col-12
"
>
<
div
class
=
"
form-check
"
>
<
input
class
=
"
form-check-input
"
type
=
"
checkbox
"
id
=
"
gridCheck
"
>
<
label
class
=
"
form-check-label
"
for
=
"
gridCheck
"
>
Check me out
</
label
>
</
div
>
</
div
>
<
div
class
=
"
col-12
"
>
<
button
type
=
"
submit
"
class
=
"
btn btn-primary
"
>
Sign in
</
button
>
</
div
>
</
form
>
Horizontal form
Create horizontal forms with the grid by adding the
.row
class to form groups and using the
.col-*-*
classes to specify the width of your labels and controls. Be sure to add
.col-form-label
to your
<label>
s as well so they’re vertically centered with their associated form controls.
At times, you maybe need to use margin or padding utilities to create that perfect alignment you need. For example, we’ve removed the
padding-top
on our stacked radio inputs label to better align the text baseline.
html
<
form
>
<
div
class
=
"
row mb-3
"
>
<
label
for
=
"
inputEmail3
"
class
=
"
col-sm-2 col-form-label
"
>
Email
</
label
>
<
div
class
=
"
col-sm-10
"
>
<
input
type
=
"
email
"
class
=
"
form-control
"
id
=
"
inputEmail3
"
>
</
div
>
</
div
>
<
div
class
=
"
row mb-3
"
>
<
label
for
=
"
inputPassword3
"
class
=
"
col-sm-2 col-form-label
"
>
Password
</
label
>
<
div
class
=
"
col-sm-10
"
>
<
input
type
=
"
password
"
class
=
"
form-control
"
id
=
"
inputPassword3
"
>
</
div
>
</
div
>
<
fieldset
class
=
"
row mb-3
"
>
<
legend
class
=
"
col-form-label col-sm-2 pt-0
"
>
Radios
</
legend
>
<
div
class
=
"
col-sm-10
"
>
<
div
class
=
"
form-check
"
>
<
input
class
=
"
form-check-input
"
type
=
"
radio
"
name
=
"
gridRadios
"
id
=
"
gridRadios1
"
value
=
"
option1
"
checked
>
<
label
class
=
"
form-check-label
"
for
=
"
gridRadios1
"
>
First radio
</
label
>
</
div
>
<
div
class
=
"
form-check
"
>
<
input
class
=
"
form-check-input
"
type
=
"
radio
"
name
=
"
gridRadios
"
id
=
"
gridRadios2
"
value
=
"
option2
"
>
<
label
class
=
"
form-check-label
"
for
=
"
gridRadios2
"
>
Second radio
</
label
>
</
div
>
<
div
class
=
"
form-check disabled
"
>
<
input
class
=
"
form-check-input
"
type
=
"
radio
"
name
=
"
gridRadios
"
id
=
"
gridRadios3
"
value
=
"
option3
"
disabled
>
<
label
class
=
"
form-check-label
"
for
=
"
gridRadios3
"
>
Third disabled radio
</
label
>
</
div
>
</
div
>
</
fieldset
>
<
div
class
=
"
row mb-3
"
>
<
div
class
=
"
col-sm-10 offset-sm-2
"
>
<
div
class
=
"
form-check
"
>
<
input
class
=
"
form-check-input
"
type
=
"
checkbox
"
id
=
"
gridCheck1
"
>
<
label
class
=
"
form-check-label
"
for
=
"
gridCheck1
"
>
Example checkbox
</
label
>
</
div
>
</
div
>
</
div
>
<
button
type
=
"
submit
"
class
=
"
btn btn-primary
"
>
Sign in
</
button
>
</
form
>
Horizontal form label sizing
Be sure to use
.col-form-label-sm
or
.col-form-label-lg
to your
<label>
s or
<legend>
s to correctly follow the size of
.form-control-lg
and
.form-control-sm
.
Email
Email
Email
html
<
div
class
=
"
row mb-3
"
>
<
label
for
=
"
colFormLabelSm
"
class
=
"
col-sm-2 col-form-label col-form-label-sm
"
>
Email
</
label
>
<
div
class
=
"
col-sm-10
"
>
<
input
type
=
"
email
"
class
=
"
form-control form-control-sm
"
id
=
"
colFormLabelSm
"
placeholder
=
"
col-form-label-sm
"
>
</
div
>
</
div
>
<
div
class
=
"
row mb-3
"
>
<
label
for
=
"
colFormLabel
"
class
=
"
col-sm-2 col-form-label
"
>
Email
</
label
>
<
div
class
=
"
col-sm-10
"
>
<
input
type
=
"
email
"
class
=
"
form-control
"
id
=
"
colFormLabel
"
placeholder
=
"
col-form-label
"
>
</
div
>
</
div
>
<
div
class
=
"
row
"
>
<
label
for
=
"
colFormLabelLg
"
class
=
"
col-sm-2 col-form-label col-form-label-lg
"
>
Email
</
label
>
<
div
class
=
"
col-sm-10
"
>
<
input
type
=
"
email
"
class
=
"
form-control form-control-lg
"
id
=
"
colFormLabelLg
"
placeholder
=
"
col-form-label-lg
"
>
</
div
>
</
div
>
Column sizing
As shown in the previous examples, our grid system allows you to place any number of
.col
s within a
.row
. They’ll split the available width equally between them. You may also pick a subset of your columns to take up more or less space, while the remaining
.col
s equally split the rest, with specific column classes like
.col-sm-7
.
html
<
div
class
=
"
row g-3
"
>
<
div
class
=
"
col-sm-7
"
>
<
input
type
=
"
text
"
class
=
"
form-control
"
placeholder
=
"
City
"
aria-label
=
"
City
"
>
</
div
>
<
div
class
=
"
col-sm
"
>
<
input
type
=
"
text
"
class
=
"
form-control
"
placeholder
=
"
State
"
aria-label
=
"
State
"
>
</
div
>
<
div
class
=
"
col-sm
"
>
<
input
type
=
"
text
"
class
=
"
form-control
"
placeholder
=
"
Zip
"
aria-label
=
"
Zip
"
>
</
div
>
</
div
>
Auto-sizing
The example below uses a flexbox utility to vertically center the contents and changes
.col
to
.col-auto
so that your columns only take up as much space as needed. Put another way, the column sizes itself based on the contents.
html
<
form
class
=
"
row gy-2 gx-3 align-items-center
"
>
<
div
class
=
"
col-auto
"
>
<
label
class
=
"
visually-hidden
"
for
=
"
autoSizingInput
"
>
Name
</
label
>
<
input
type
=
"
text
"
class
=
"
form-control
"
id
=
"
autoSizingInput
"
placeholder
=
"
Jane Doe
"
>
</
div
>
<
div
class
=
"
col-auto
"
>
<
label
class
=
"
visually-hidden
"
for
=
"
autoSizingInputGroup
"
>
Username
</
label
>
<
div
class
=
"
input-group
"
>
<
div
class
=
"
input-group-text
"
>
@
</
div
>
<
input
type
=
"
text
"
class
=
"
form-control
"
id
=
"
autoSizingInputGroup
"
placeholder
=
"
Username
"
>
</
div
>
</
div
>
<
div
class
=
"
col-auto
"
>
<
label
class
=
"
visually-hidden
"
for
=
"
autoSizingSelect
"
>
Preference
</
label
>
<
select
class
=
"
form-select
"
id
=
"
autoSizingSelect
"
>
<
option
selected
>
Choose...
</
option
>
<
option
value
=
"
1
"
>
One
</
option
>
<
option
value
=
"
2
"
>
Two
</
option
>
<
option
value
=
"
3
"
>
Three
</
option
>
</
select
>
</
div
>
<
div
class
=
"
col-auto
"
>
<
div
class
=
"
form-check
"
>
<
input
class
=
"
form-check-input
"
type
=
"
checkbox
"
id
=
"
autoSizingCheck
"
>
<
label
class
=
"
form-check-label
"
for
=
"
autoSizingCheck
"
>
Remember me
</
label
>
</
div
>
</
div
>
<
div
class
=
"
col-auto
"
>
<
button
type
=
"
submit
"
class
=
"
btn btn-primary
"
>
Submit
</
button
>
</
div
>
</
form
>
You can then remix that once again with size-specific column classes.
html
<
form
class
=
"
row gx-3 gy-2 align-items-center
"
>
<
div
class
=
"
col-sm-3
"
>
<
label
class
=
"
visually-hidden
"
for
=
"
specificSizeInputName
"
>
Name
</
label
>
<
input
type
=
"
text
"
class
=
"
form-control
"
id
=
"
specificSizeInputName
"
placeholder
=
"
Jane Doe
"
>
</
div
>
<
div
class
=
"
col-sm-3
"
>
<
label
class
=
"
visually-hidden
"
for
=
"
specificSizeInputGroupUsername
"
>
Username
</
label
>
<
div
class
=
"
input-group
"
>
<
div
class
=
"
input-group-text
"
>
@
</
div
>
<
input
type
=
"
text
"
class
=
"
form-control
"
id
=
"
specificSizeInputGroupUsername
"
placeholder
=
"
Username
"
>
</
div
>
</
div
>
<
div
class
=
"
col-sm-3
"
>
<
label
class
=
"
visually-hidden
"
for
=
"
specificSizeSelect
"
>
Preference
</
label
>
<
select
class
=
"
form-select
"
id
=
"
specificSizeSelect
"
>
<
option
selected
>
Choose...
</
option
>
<
option
value
=
"
1
"
>
One
</
option
>
<
option
value
=
"
2
"
>
Two
</
option
>
<
option
value
=
"
3
"
>
Three
</
option
>
</
select
>
</
div
>
<
div
class
=
"
col-auto
"
>
<
div
class
=
"
form-check
"
>
<
input
class
=
"
form-check-input
"
type
=
"
checkbox
"
id
=
"
autoSizingCheck2
"
>
<
label
class
=
"
form-check-label
"
for
=
"
autoSizingCheck2
"
>
Remember me
</
label
>
</
div
>
</
div
>
<
div
class
=
"
col-auto
"
>
<
button
type
=
"
submit
"
class
=
"
btn btn-primary
"
>
Submit
</
button
>
</
div
>
</
form
>
Inline forms
Use the
.row-cols-*
classes to create responsive horizontal layouts. By adding
gutter modifier classes
, we'll have gutters in horizontal and vertical directions. On narrow mobile viewports, the
.col-12
helps stack the form controls and more. The
.align-items-center
aligns the form elements to the middle, making the
.form-check
align properly.
html
<
form
class
=
"
row row-cols-lg-auto g-3 align-items-center
"
>
<
div
class
=
"
col-12
"
>
<
label
class
=
"
visually-hidden
"
for
=
"
inlineFormInputGroupUsername
"
>
Username
</
label
>
<
div
class
=
"
input-group
"
>
<
div
class
=
"
input-group-text
"
>
@
</
div
>
<
input
type
=
"
text
"
class
=
"
form-control
"
id
=
"
inlineFormInputGroupUsername
"
placeholder
=
"
Username
"
>
</
div
>
</
div
>
<
div
class
=
"
col-12
"
>
<
label
class
=
"
visually-hidden
"
for
=
"
inlineFormSelectPref
"
>
Preference
</
label
>
<
select
class
=
"
form-select
"
id
=
"
inlineFormSelectPref
"
>
<
option
selected
>
Choose...
</
option
>
<
option
value
=
"
1
"
>
One
</
option
>
<
option
value
=
"
2
"
>
Two
</
option
>
<
option
value
=
"
3
"
>
Three
</
option
>
</
select
>
</
div
>
<
div
class
=
"
col-12
"
>
<
div
class
=
"
form-check
"
>
<
input
class
=
"
form-check-input
"
type
=
"
checkbox
"
id
=
"
inlineFormCheck
"
>
<
label
class
=
"
form-check-label
"
for
=
"
inlineFormCheck
"
>
Remember me
</
label
>
</
div
>
</
div
>
<
div
class
=
"
col-12
"
>
<
button
type
=
"
submit
"
class
=
"
btn btn-primary
"
>
Submit
</
button
>
</
div
>
</
form
>


## Validation · Bootstrap v5.3
- source: https://getbootstrap.com/docs/5.3/forms/validation/
- fetched_at: 2026-04-29T13:46:06.108755+00:00

View on GitHub
Validation
Provide valuable, actionable feedback to your users with HTML5 form validation, via browser default behaviors or custom styles and JavaScript.
On this page
We are aware that currently the client-side custom validation styles and tooltips are not accessible, since they are not exposed to assistive technologies. While we work on a solution, we’d recommend either using the server-side option or the default browser validation method.
How it works
Here’s how form validation works with Bootstrap:
HTML form validation is applied via CSS’s two pseudo-classes,
:invalid
and
:valid
. It applies to
<input>
,
<select>
, and
<textarea>
elements.
Bootstrap scopes the
:invalid
and
:valid
styles to parent
.was-validated
class, usually applied to the
<form>
. Otherwise, any required field without a value shows up as invalid on page load. This way, you may choose when to activate them (typically after form submission is attempted).
To reset the appearance of the form (for instance, in the case of dynamic form submissions using Ajax), remove the
.was-validated
class from the
<form>
again after submission.
As a fallback,
.is-invalid
and
.is-valid
classes may be used instead of the pseudo-classes for
server-side validation
. They do not require a
.was-validated
parent class.
Due to constraints in how CSS works, we cannot (at present) apply styles to a
<label>
that comes before a form control in the DOM without the help of custom JavaScript.
All modern browsers support the
constraint validation API
, a series of JavaScript methods for validating form controls.
Feedback messages may utilize the
browser defaults
(different for each browser, and unstylable via CSS) or our custom feedback styles with additional HTML and CSS.
You may provide custom validity messages with
setCustomValidity
in JavaScript.
With that in mind, consider the following demos for our custom form validation styles, optional server-side classes, and browser defaults.
Custom styles
For custom Bootstrap form validation messages, you’ll need to add the
novalidate
boolean attribute to your
<form>
. This disables the browser default feedback tooltips, but still provides access to the form validation APIs in JavaScript. Try to submit the form below; our JavaScript will intercept the submit button and relay feedback to you. When attempting to submit, you’ll see the
:invalid
and
:valid
styles applied to your form controls.
Custom feedback styles apply custom colors, borders, focus styles, and background icons to better communicate feedback. Background icons for
<select>
s are only available with
.form-select
, and not
.form-control
.
html
<
form
class
=
"
row g-3 needs-validation
"
novalidate
>
<
div
class
=
"
col-md-4
"
>
<
label
for
=
"
validationCustom01
"
class
=
"
form-label
"
>
First name
</
label
>
<
input
type
=
"
text
"
class
=
"
form-control
"
id
=
"
validationCustom01
"
value
=
"
Mark
"
required
>
<
div
class
=
"
valid-feedback
"
>
Looks good!
</
div
>
</
div
>
<
div
class
=
"
col-md-4
"
>
<
label
for
=
"
validationCustom02
"
class
=
"
form-label
"
>
Last name
</
label
>
<
input
type
=
"
text
"
class
=
"
form-control
"
id
=
"
validationCustom02
"
value
=
"
Otto
"
required
>
<
div
class
=
"
valid-feedback
"
>
Looks good!
</
div
>
</
div
>
<
div
class
=
"
col-md-4
"
>
<
label
for
=
"
validationCustomUsername
"
class
=
"
form-label
"
>
Username
</
label
>
<
div
class
=
"
input-group has-validation
"
>
<
span
class
=
"
input-group-text
"
id
=
"
inputGroupPrepend
"
>
@
</
span
>
<
input
type
=
"
text
"
class
=
"
form-control
"
id
=
"
validationCustomUsername
"
aria-describedby
=
"
inputGroupPrepend
"
required
>
<
div
class
=
"
invalid-feedback
"
>
Please choose a username.
</
div
>
</
div
>
</
div
>
<
div
class
=
"
col-md-6
"
>
<
label
for
=
"
validationCustom03
"
class
=
"
form-label
"
>
City
</
label
>
<
input
type
=
"
text
"
class
=
"
form-control
"
id
=
"
validationCustom03
"
required
>
<
div
class
=
"
invalid-feedback
"
>
Please provide a valid city.
</
div
>
</
div
>
<
div
class
=
"
col-md-3
"
>
<
label
for
=
"
validationCustom04
"
class
=
"
form-label
"
>
State
</
label
>
<
select
class
=
"
form-select
"
id
=
"
validationCustom04
"
required
>
<
option
selected
disabled
value
=
"
"
>
Choose...
</
option
>
<
option
>
...
</
option
>
</
select
>
<
div
class
=
"
invalid-feedback
"
>
Please select a valid state.
</
div
>
</
div
>
<
div
class
=
"
col-md-3
"
>
<
label
for
=
"
validationCustom05
"
class
=
"
form-label
"
>
Zip
</
label
>
<
input
type
=
"
text
"
class
=
"
form-control
"
id
=
"
validationCustom05
"
required
>
<
div
class
=
"
invalid-feedback
"
>
Please provide a valid zip.
</
div
>
</
div
>
<
div
class
=
"
col-12
"
>
<
div
class
=
"
form-check
"
>
<
input
class
=
"
form-check-input
"
type
=
"
checkbox
"
value
=
"
"
id
=
"
invalidCheck
"
required
>
<
label
class
=
"
form-check-label
"
for
=
"
invalidCheck
"
>
Agree to terms and conditions
</
label
>
<
div
class
=
"
invalid-feedback
"
>
You must agree before submitting.
</
div
>
</
div
>
</
div
>
<
div
class
=
"
col-12
"
>
<
button
class
=
"
btn btn-primary
"
type
=
"
submit
"
>
Submit form
</
button
>
</
div
>
</
form
>
// Example starter JavaScript for disabling form submissions if there are invalid fields
(
(
)
=>
{
'use strict'
// Fetch all the forms we want to apply custom Bootstrap validation styles to
const
forms
=
document
.
querySelectorAll
(
'.needs-validation'
)
// Loop over them and prevent submission
Array
.
from
(
forms
)
.
forEach
(
form
=>
{
form
.
addEventListener
(
'submit'
,
event
=>
{
if
(
!
form
.
checkValidity
(
)
)
{
event
.
preventDefault
(
)
event
.
stopPropagation
(
)
}
form
.
classList
.
add
(
'was-validated'
)
}
,
false
)
}
)
}
)
(
)
Browser defaults
Not interested in custom validation feedback messages or writing JavaScript to change form behaviors? All good, you can use the browser defaults. Try submitting the form below. Depending on your browser and OS, you’ll see a slightly different style of feedback.
While these feedback styles cannot be styled with CSS, you can still customize the feedback text through JavaScript.
html
<
form
class
=
"
row g-3
"
>
<
div
class
=
"
col-md-4
"
>
<
label
for
=
"
validationDefault01
"
class
=
"
form-label
"
>
First name
</
label
>
<
input
type
=
"
text
"
class
=
"
form-control
"
id
=
"
validationDefault01
"
value
=
"
Mark
"
required
>
</
div
>
<
div
class
=
"
col-md-4
"
>
<
label
for
=
"
validationDefault02
"
class
=
"
form-label
"
>
Last name
</
label
>
<
input
type
=
"
text
"
class
=
"
form-control
"
id
=
"
validationDefault02
"
value
=
"
Otto
"
required
>
</
div
>
<
div
class
=
"
col-md-4
"
>
<
label
for
=
"
validationDefaultUsername
"
class
=
"
form-label
"
>
Username
</
label
>
<
div
class
=
"
input-group
"
>
<
span
class
=
"
input-group-text
"
id
=
"
inputGroupPrepend2
"
>
@
</
span
>
<
input
type
=
"
text
"
class
=
"
form-control
"
id
=
"
validationDefaultUsername
"
aria-describedby
=
"
inputGroupPrepend2
"
required
>
</
div
>
</
div
>
<
div
class
=
"
col-md-6
"
>
<
label
for
=
"
validationDefault03
"
class
=
"
form-label
"
>
City
</
label
>
<
input
type
=
"
text
"
class
=
"
form-control
"
id
=
"
validationDefault03
"
required
>
</
div
>
<
div
class
=
"
col-md-3
"
>
<
label
for
=
"
validationDefault04
"
class
=
"
form-label
"
>
State
</
label
>
<
select
class
=
"
form-select
"
id
=
"
validationDefault04
"
required
>
<
option
selected
disabled
value
=
"
"
>
Choose...
</
option
>
<
option
>
...
</
option
>
</
select
>
</
div
>
<
div
class
=
"
col-md-3
"
>
<
label
for
=
"
validationDefault05
"
class
=
"
form-label
"
>
Zip
</
label
>
<
input
type
=
"
text
"
class
=
"
form-control
"
id
=
"
validationDefault05
"
required
>
</
div
>
<
div
class
=
"
col-12
"
>
<
div
class
=
"
form-check
"
>
<
input
class
=
"
form-check-input
"
type
=
"
checkbox
"
value
=
"
"
id
=
"
invalidCheck2
"
required
>
<
label
class
=
"
form-check-label
"
for
=
"
invalidCheck2
"
>
Agree to terms and conditions
</
label
>
</
div
>
</
div
>
<
div
class
=
"
col-12
"
>
<
button
class
=
"
btn btn-primary
"
type
=
"
submit
"
>
Submit form
</
button
>
</
div
>
</
form
>
Server-side
We recommend using client-side validation, but in case you require server-side validation, you can indicate invalid and valid form fields with
.is-invalid
and
.is-valid
. Note that
.invalid-feedback
is also supported with these classes.
For invalid fields, ensure that the invalid feedback/error message is associated with the relevant form field using
aria-describedby
(noting that this attribute allows more than one
id
to be referenced, in case the field already points to additional form text).
To fix
issues with border radius
, input groups require an additional
.has-validation
class.
html
<
form
class
=
"
row g-3
"
>
<
div
class
=
"
col-md-4
"
>
<
label
for
=
"
validationServer01
"
class
=
"
form-label
"
>
First name
</
label
>
<
input
type
=
"
text
"
class
=
"
form-control is-valid
"
id
=
"
validationServer01
"
value
=
"
Mark
"
required
>
<
div
class
=
"
valid-feedback
"
>
Looks good!
</
div
>
</
div
>
<
div
class
=
"
col-md-4
"
>
<
label
for
=
"
validationServer02
"
class
=
"
form-label
"
>
Last name
</
label
>
<
input
type
=
"
text
"
class
=
"
form-control is-valid
"
id
=
"
validationServer02
"
value
=
"
Otto
"
required
>
<
div
class
=
"
valid-feedback
"
>
Looks good!
</
div
>
</
div
>
<
div
class
=
"
col-md-4
"
>
<
label
for
=
"
validationServerUsername
"
class
=
"
form-label
"
>
Username
</
label
>
<
div
class
=
"
input-group has-validation
"
>
<
span
class
=
"
input-group-text
"
id
=
"
inputGroupPrepend3
"
>
@
</
span
>
<
input
type
=
"
text
"
class
=
"
form-control is-invalid
"
id
=
"
validationServerUsername
"
aria-describedby
=
"
inputGroupPrepend3 validationServerUsernameFeedback
"
required
>
<
div
id
=
"
validationServerUsernameFeedback
"
class
=
"
invalid-feedback
"
>
Please choose a username.
</
div
>
</
div
>
</
div
>
<
div
class
=
"
col-md-6
"
>
<
label
for
=
"
validationServer03
"
class
=
"
form-label
"
>
City
</
label
>
<
input
type
=
"
text
"
class
=
"
form-control is-invalid
"
id
=
"
validationServer03
"
aria-describedby
=
"
validationServer03Feedback
"
required
>
<
div
id
=
"
validationServer03Feedback
"
class
=
"
invalid-feedback
"
>
Please provide a valid city.
</
div
>
</
div
>
<
div
class
=
"
col-md-3
"
>
<
label
for
=
"
validationServer04
"
class
=
"
form-label
"
>
State
</
label
>
<
select
class
=
"
form-select is-invalid
"
id
=
"
validationServer04
"
aria-describedby
=
"
validationServer04Feedback
"
required
>
<
option
selected
disabled
value
=
"
"
>
Choose...
</
option
>
<
option
>
...
</
option
>
</
select
>
<
div
id
=
"
validationServer04Feedback
"
class
=
"
invalid-feedback
"
>
Please select a valid state.
</
div
>
</
div
>
<
div
class
=
"
col-md-3
"
>
<
label
for
=
"
validationServer05
"
class
=
"
form-label
"
>
Zip
</
label
>
<
input
type
=
"
text
"
class
=
"
form-control is-invalid
"
id
=
"
validationServer05
"
aria-describedby
=
"
validationServer05Feedback
"
required
>
<
div
id
=
"
validationServer05Feedback
"
class
=
"
invalid-feedback
"
>
Please provide a valid zip.
</
div
>
</
div
>
<
div
class
=
"
col-12
"
>
<
div
class
=
"
form-check
"
>
<
input
class
=
"
form-check-input is-invalid
"
type
=
"
checkbox
"
value
=
"
"
id
=
"
invalidCheck3
"
aria-describedby
=
"
invalidCheck3Feedback
"
required
>
<
label
class
=
"
form-check-label
"
for
=
"
invalidCheck3
"
>
Agree to terms and conditions
</
label
>
<
div
id
=
"
invalidCheck3Feedback
"
class
=
"
invalid-feedback
"
>
You must agree before submitting.
</
div
>
</
div
>
</
div
>
<
div
class
=
"
col-12
"
>
<
button
class
=
"
btn btn-primary
"
type
=
"
submit
"
>
Submit form
</
button
>
</
div
>
</
form
>
Supported elements
Validation styles are available for the following form controls and components:
<input>
s and
<textarea>
s with
.form-control
(including up to one
.form-control
in input groups)
<select>
s with
.form-select
.form-check
s
html
<
form
class
=
"
was-validated
"
>
<
div
class
=
"
mb-3
"
>
<
label
for
=
"
validationTextarea
"
class
=
"
form-label
"
>
Textarea
</
label
>
<
textarea
class
=
"
form-control
"
id
=
"
validationTextarea
"
placeholder
=
"
Required example textarea
"
required
>
</
textarea
>
<
div
class
=
"
invalid-feedback
"
>
Please enter a message in the textarea.
</
div
>
</
div
>
<
div
class
=
"
form-check mb-3
"
>
<
input
type
=
"
checkbox
"
class
=
"
form-check-input
"
id
=
"
validationFormCheck1
"
required
>
<
label
class
=
"
form-check-label
"
for
=
"
validationFormCheck1
"
>
Check this checkbox
</
label
>
<
div
class
=
"
invalid-feedback
"
>
Example invalid feedback text
</
div
>
</
div
>
<
div
class
=
"
form-check
"
>
<
input
type
=
"
radio
"
class
=
"
form-check-input
"
id
=
"
validationFormCheck2
"
name
=
"
radio-stacked
"
required
>
<
label
class
=
"
form-check-label
"
for
=
"
validationFormCheck2
"
>
Toggle this radio
</
label
>
</
div
>
<
div
class
=
"
form-check mb-3
"
>
<
input
type
=
"
radio
"
class
=
"
form-check-input
"
id
=
"
validationFormCheck3
"
name
=
"
radio-stacked
"
required
>
<
label
class
=
"
form-check-label
"
for
=
"
validationFormCheck3
"
>
Or toggle this other radio
</
label
>
<
div
class
=
"
invalid-feedback
"
>
More example invalid feedback text
</
div
>
</
div
>
<
div
class
=
"
mb-3
"
>
<
select
class
=
"
form-select
"
required
aria-label
=
"
select example
"
>
<
option
value
=
"
"
>
Open this select menu
</
option
>
<
option
value
=
"
1
"
>
One
</
option
>
<
option
value
=
"
2
"
>
Two
</
option
>
<
option
value
=
"
3
"
>
Three
</
option
>
</
select
>
<
div
class
=
"
invalid-feedback
"
>
Example invalid select feedback
</
div
>
</
div
>
<
div
class
=
"
mb-3
"
>
<
input
type
=
"
file
"
class
=
"
form-control
"
aria-label
=
"
file example
"
required
>
<
div
class
=
"
invalid-feedback
"
>
Example invalid form file feedback
</
div
>
</
div
>
<
div
class
=
"
mb-3
"
>
<
button
class
=
"
btn btn-primary
"
type
=
"
submit
"
disabled
>
Submit form
</
button
>
</
div
>
</
form
>
Tooltips
If your form layout allows it, you can swap the
.{valid|invalid}-feedback
classes for
.{valid|invalid}-tooltip
classes to display validation feedback in a styled tooltip. Be sure to have a parent with
position: relative
on it for tooltip positioning. In the example below, our column classes have this already, but your project may require an alternative setup.
html
<
form
class
=
"
row g-3 needs-validation
"
novalidate
>
<
div
class
=
"
col-md-4 position-relative
"
>
<
label
for
=
"
validationTooltip01
"
class
=
"
form-label
"
>
First name
</
label
>
<
input
type
=
"
text
"
class
=
"
form-control
"
id
=
"
validationTooltip01
"
value
=
"
Mark
"
required
>
<
div
class
=
"
valid-tooltip
"
>
Looks good!
</
div
>
</
div
>
<
div
class
=
"
col-md-4 position-relative
"
>
<
label
for
=
"
validationTooltip02
"
class
=
"
form-label
"
>
Last name
</
label
>
<
input
type
=
"
text
"
class
=
"
form-control
"
id
=
"
validationTooltip02
"
value
=
"
Otto
"
required
>
<
div
class
=
"
valid-tooltip
"
>
Looks good!
</
div
>
</
div
>
<
div
class
=
"
col-md-4 position-relative
"
>
<
label
for
=
"
validationTooltipUsername
"
class
=
"
form-label
"
>
Username
</
label
>
<
div
class
=
"
input-group has-validation
"
>
<
span
class
=
"
input-group-text
"
id
=
"
validationTooltipUsernamePrepend
"
>
@
</
span
>
<
input
type
=
"
text
"
class
=
"
form-control
"
id
=
"
validationTooltipUsername
"
aria-describedby
=
"
validationTooltipUsernamePrepend
"
required
>
<
div
class
=
"
invalid-tooltip
"
>
Please choose a unique and valid username.
</
div
>
</
div
>
</
div
>
<
div
class
=
"
col-md-6 position-relative
"
>
<
label
for
=
"
validationTooltip03
"
class
=
"
form-label
"
>
City
</
label
>
<
input
type
=
"
text
"
class
=
"
form-control
"
id
=
"
validationTooltip03
"
required
>
<
div
class
=
"
invalid-tooltip
"
>
Please provide a valid city.
</
div
>
</
div
>
<
div
class
=
"
col-md-3 position-relative
"
>
<
label
for
=
"
validationTooltip04
"
class
=
"
form-label
"
>
State
</
label
>
<
select
class
=
"
form-select
"
id
=
"
validationTooltip04
"
required
>
<
option
selected
disabled
value
=
"
"
>
Choose...
</
option
>
<
option
>
...
</
option
>
</
select
>
<
div
class
=
"
invalid-tooltip
"
>
Please select a valid state.
</
div
>
</
div
>
<
div
class
=
"
col-md-3 position-relative
"
>
<
label
for
=
"
validationTooltip05
"
class
=
"
form-label
"
>
Zip
</
label
>
<
input
type
=
"
text
"
class
=
"
form-control
"
id
=
"
validationTooltip05
"
required
>
<
div
class
=
"
invalid-tooltip
"
>
Please provide a valid zip.
</
div
>
</
div
>
<
div
class
=
"
col-12
"
>
<
button
class
=
"
btn btn-primary
"
type
=
"
submit
"
>
Submit form
</
button
>
</
div
>
</
form
>
CSS
Variables
Added in v5.3.0
As part of Bootstrap’s evolving CSS variables approach, forms now use local CSS variables for validation for enhanced real-time customization. Values for the CSS variables are set via Sass, so Sass customization is still supported, too.
scss/_root.scss
--
#{$prefix}
form-valid-color
:
#{$form-valid-color}
;
--
#{$prefix}
form-valid-border-color
:
#{$form-valid-border-color}
;
--
#{$prefix}
form-invalid-color
:
#{$form-invalid-color}
;
--
#{$prefix}
form-invalid-border-color
:
#{$form-invalid-border-color}
;
These variables are also color mode adaptive, meaning they change color while in dark mode.
Sass variables
scss/_variables.scss
$form-feedback-margin-top
:
$form-text-margin-top
;
$form-feedback-font-size
:
$form-text-font-size
;
$form-feedback-font-style
:
$form-text-font-style
;
$form-feedback-valid-color
:
$success
;
$form-feedback-invalid-color
:
$danger
;
$form-feedback-icon-valid-color
:
$form-feedback-valid-color
;
$form-feedback-icon-valid
:
url
(
"data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'><path fill='#{$form-feedback-icon-valid-color}' d='M2.3 6.73.6 4.53c-.4-1.04.46-1.4 1.1-.8l1.1 1.4 3.4-3.8c.6-.63 1.6-.27 1.2.7l-4 4.6c-.43.5-.8.4-1.1.1'/></svg>"
)
;
$form-feedback-icon-invalid-color
:
$form-feedback-invalid-color
;
$form-feedback-icon-invalid
:
url
(
"data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12' width='12' height='12' fill='none' stroke='#{$form-feedback-icon-invalid-color}'><circle cx='6' cy='6' r='4.5'/><path stroke-linejoin='round' d='M5.8 3.6h.4L6 6.5z'/><circle cx='6' cy='8.2' r='.6' fill='#{$form-feedback-icon-invalid-color}' stroke='none'/></svg>"
)
;
scss/_variables.scss
$form-valid-color
:
$form-feedback-valid-color
;
$form-valid-border-color
:
$form-feedback-valid-color
;
$form-invalid-color
:
$form-feedback-invalid-color
;
$form-invalid-border-color
:
$form-feedback-invalid-color
;
scss/_variables-dark.scss
$form-valid-color-dark
:
$green-300
;
$form-valid-border-color-dark
:
$green-300
;
$form-invalid-color-dark
:
$red-300
;
$form-invalid-border-color-dark
:
$red-300
;
Sass mixins
Two mixins are combined, through our
loop
, to generate our form validation feedback styles.
scss/mixins/_forms.scss
@mixin
form-validation-state-selector
(
$state
)
{
@if
(
$state
==
"valid"
or
$state
==
"invalid"
)
{
.was-validated #
{
if
(
&
,
"&"
,
""
)
}
:
#{$state}
,
#
{
if
(
&
,
"&"
,
""
)
}
.is-
#{$state}
{
@content
;
}
}
@else
{
#
{
if
(
&
,
"&"
,
""
)
}
.is-
#{$state}
{
@content
;
}
}
}
@mixin
form-validation-state
(
$state
,
$color
,
$icon
,
$tooltip-color
:
color-contrast
(
$color
)
,
$tooltip-bg-color
:
rgba
(
$color
,
$form-feedback-tooltip-opacity
)
,
$focus-box-shadow
:
0 0
$input-btn-focus-blur
$input-focus-width
rgba
(
$color
,
$input-btn-focus-color-opacity
)
,
$border-color
:
$color
)
{
.
#{$state}
-feedback
{
display
:
none
;
width
:
100%
;
margin-top
:
$form-feedback-margin-top
;
@include
font-size
(
$form-feedback-font-size
)
;
font-style
:
$form-feedback-font-style
;
color
:
$color
;
}
.
#{$state}
-tooltip
{
position
:
absolute
;
top
:
100%
;
z-index
:
5
;
display
:
none
;
max-width
:
100%
;
// Contain to parent when possible
padding
:
$form-feedback-tooltip-padding-y
$form-feedback-tooltip-padding-x
;
margin-top
:
.1rem
;
@include
font-size
(
$form-feedback-tooltip-font-size
)
;
line-height
:
$form-feedback-tooltip-line-height
;
color
:
$tooltip-color
;
background-color
:
$tooltip-bg-color
;
@include
border-radius
(
$form-feedback-tooltip-border-radius
)
;
}
@include
form-validation-state-selector
(
$state
)
{
~ .
#{$state}
-feedback,
 ~ .
#{$state}
-tooltip
{
display
:
block
;
}
}
.form-control
{
@include
form-validation-state-selector
(
$state
)
{
border-color
:
$border-color
;
@if
$enable-validation-icons
{
padding-right
:
$input-height-inner
;
background-image
:
escape-svg
(
$icon
)
;
background-repeat
:
no-repeat
;
background-position
:
right
$input-height-inner-quarter
center
;
background-size
:
$input-height-inner-half
$input-height-inner-half
;
}
&
:focus
{
border-color
:
$border-color
;
@if
$enable-shadows
{
@include
box-shadow
(
$input-box-shadow
,
$focus-box-shadow
)
;
}
@else
{
// Avoid using mixin so we can pass custom focus shadow properly
box-shadow
:
$focus-box-shadow
;
}
}
}
}
// stylelint-disable-next-line selector-no-qualifying-type
textarea.form-control
{
@include
form-validation-state-selector
(
$state
)
{
@if
$enable-validation-icons
{
padding-right
:
$input-height-inner
;
background-position
:
top
$input-height-inner-quarter
right
$input-height-inner-quarter
;
}
}
}
.form-select
{
@include
form-validation-state-selector
(
$state
)
{
border-color
:
$border-color
;
@if
$enable-validation-icons
{
&
:
not
(
[multiple]
)
:
not
(
[size]
)
,
&
:
not
(
[multiple]
)
[size="1"]
{
--
#{$prefix}
form-select-bg-icon
:
#
{
escape-svg
(
$icon
)
}
;
padding-right
:
$form-select-feedback-icon-padding-end
;
background-position
:
$form-select-bg-position
,
$form-select-feedback-icon-position
;
background-size
:
$form-select-bg-size
,
$form-select-feedback-icon-size
;
}
}
&
:focus
{
border-color
:
$border-color
;
@if
$enable-shadows
{
@include
box-shadow
(
$form-select-box-shadow
,
$focus-box-shadow
)
;
}
@else
{
// Avoid using mixin so we can pass custom focus shadow properly
box-shadow
:
$focus-box-shadow
;
}
}
}
}
.form-control-color
{
@include
form-validation-state-selector
(
$state
)
{
@if
$enable-validation-icons
{
width
:
add
(
$form-color-width
,
$input-height-inner
)
;
}
}
}
.form-check-input
{
@include
form-validation-state-selector
(
$state
)
{
border-color
:
$border-color
;
&
:checked
{
background-color
:
$color
;
}
&
:focus
{
box-shadow
:
$focus-box-shadow
;
}
~ .form-check-label
{
color
:
$color
;
}
}
}
.form-check-inline .form-check-input
{
~ .
#{$state}
-feedback
{
margin-left
:
.5em
;
}
}
.input-group
{
>
.
form-control
:
not
(
:
focus
)
,
>
.
form-select
:
not
(
:
focus
)
,
>
.
form-floating
:
not
(
:
focus-within
)
{
@include
form-validation-state-selector
(
$state
)
{
@if
$state
== "valid"
{
z-index
:
3
;
}
@else if
$state
== "invalid"
{
z-index
:
4
;
}
}
}
}
}
Sass maps
This is the validation Sass map from
_variables.scss
. Override or extend this to generate different or additional states.
scss/_variables.scss
$form-validation-states
:
(
"valid"
:
(
"color"
:
var
(
--
#{$prefix}
form-valid-color
)
,
"icon"
:
$form-feedback-icon-valid
,
"tooltip-color"
:
#fff
,
"tooltip-bg-color"
:
var
(
--
#{$prefix}
success
)
,
"focus-box-shadow"
:
0 0
$input-btn-focus-blur
$input-focus-width
rgba
(
var
(
--
#{$prefix}
success-rgb
)
,
$input-btn-focus-color-opacity
)
,
"border-color"
:
var
(
--
#{$prefix}
form-valid-border-color
)
,
)
,
"invalid"
:
(
"color"
:
var
(
--
#{$prefix}
form-invalid-color
)
,
"icon"
:
$form-feedback-icon-invalid
,
"tooltip-color"
:
#fff
,
"tooltip-bg-color"
:
var
(
--
#{$prefix}
danger
)
,
"focus-box-shadow"
:
0 0
$input-btn-focus-blur
$input-focus-width
rgba
(
var
(
--
#{$prefix}
danger-rgb
)
,
$input-btn-focus-color-opacity
)
,
"border-color"
:
var
(
--
#{$prefix}
form-invalid-border-color
)
,
)
)
;
Maps of
$form-validation-states
can contain three optional parameters to override tooltips and focus styles.
Sass loops
Used to iterate over
$form-validation-states
map values to generate our validation styles. Any modifications to the above Sass map will be reflected in your compiled CSS via this loop.
scss/forms/_validation.scss
@each
$state
,
$data
in
$form-validation-states
{
@include
form-validation-state
(
$state
,
$data
...
)
;
}
Customizing
Validation states can be customized via Sass with the
$form-validation-states
map. Located in our
_variables.scss
file, this Sass map is how we generate the default
valid
/
invalid
validation states. Included is a nested map for customizing each state’s color, icon, tooltip color, and focus shadow. While no other states are supported by browsers, those using custom styles can easily add more complex form feedback.

