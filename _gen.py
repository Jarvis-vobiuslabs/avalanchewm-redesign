import os

BASE = "/private/tmp/avalanchewm-redesign"

def page(filename, title, meta_desc, active_nav, og_image, content):
    nav_items = [
        ("index.html", "Home"),
        ("about.html", "About"),
        None,  # Services dropdown
        None,  # Bin Rentals dropdown
        ("portable-toilets.html", "Portable Toilets"),
        ("temporary-fencing.html", "Temporary Fencing"),
        ("contractor.html", "Contractors"),
        ("contact.html", "Contact"),
    ]

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{meta_desc}" />
  <link rel="icon" type="image/png" href="assets/logo.png" />
  <link rel="stylesheet" href="assets/style.css" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{meta_desc}" />
  <meta property="og:image" content="{og_image}" />
  <meta name="twitter:card" content="summary_large_image" />
</head>
<body>

  <div class="topbar">
    Award-winning Calgary Waste Management &nbsp;&middot;&nbsp;
    <a href="tel:4034611677">&#128222; 403-461-1677</a>
    &nbsp;&middot;&nbsp;
    <a href="mailto:info@avalanchewm.com">info@avalanchewm.com</a>
  </div>

  <nav class="site-nav">
    <div class="nav-inner">
      <a class="nav-logo" href="index.html"><img src="assets/logo.png" alt="Avalanche Waste Management" /></a>
      <input type="checkbox" id="nav-toggle" />
      <label class="hamburger" for="nav-toggle"><span></span><span></span><span></span></label>
      <ul class="nav-menu">
        <li class="nav-item"><a class="nav-link{' active' if active_nav=='home' else ''}" href="index.html">Home</a></li>
        <li class="nav-item"><a class="nav-link{' active' if active_nav=='about' else ''}" href="about.html">About</a></li>
        <li class="nav-item dropdown">
          <a class="nav-link{' active' if active_nav in ('commercial','residential') else ''}" href="#">Services <span class="caret">&#9660;</span></a>
          <div class="dropdown-menu">
            <a class="dropdown-item" href="commercial-services.html">Commercial Services</a>
            <a class="dropdown-item" href="residential-services.html">Residential Services</a>
          </div>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link{' active' if active_nav=='rentals' else ''}" href="rentals.html">Bin Rentals <span class="caret">&#9660;</span></a>
          <div class="dropdown-menu">
            <a class="dropdown-item" href="rentals.html#yard40">40-Yard Bin</a>
            <a class="dropdown-item" href="rentals.html#yard30">30-Yard Bin</a>
            <a class="dropdown-item" href="rentals.html#yard20">20-Yard Bin</a>
            <a class="dropdown-item" href="rentals.html#yard12">12-Yard Bin</a>
          </div>
        </li>
        <li class="nav-item"><a class="nav-link{' active' if active_nav=='toilets' else ''}" href="portable-toilets.html">Portable Toilets</a></li>
        <li class="nav-item"><a class="nav-link{' active' if active_nav=='fencing' else ''}" href="temporary-fencing.html">Temporary Fencing</a></li>
        <li class="nav-item"><a class="nav-link{' active' if active_nav=='contractor' else ''}" href="contractor.html">Contractors</a></li>
        <li class="nav-item"><a class="nav-link{' active' if active_nav=='contact' else ''}" href="contact.html">Contact</a></li>
      </ul>
      <div class="nav-right">
        <a class="nav-phone" href="tel:4034611677">403-461-1677</a>
        <a class="btn btn-primary btn-sm" href="booking.html">Book Now</a>
      </div>
    </div>
  </nav>

{content}

  <!-- ── Footer ─────────────────────────────────────────── -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <img src="assets/logo.png" alt="Avalanche Waste Management" />
          <p>Calgary&rsquo;s award-winning bin rental, portable toilet, and temporary fencing provider. Honest pricing, reliable service, always.</p>
          <div class="footer-social">
            <a href="https://www.facebook.com/Avalanche-Waste-Management-693811640731460" target="_blank" rel="noopener" aria-label="Facebook">f</a>
            <a href="https://twitter.com/avalanche_waste" target="_blank" rel="noopener" aria-label="Twitter">&#120143;</a>
            <a href="https://instagram.com/avalanche_waste" target="_blank" rel="noopener" aria-label="Instagram">ig</a>
          </div>
        </div>
        <div class="footer-col">
          <h4>Services</h4>
          <ul>
            <li><a href="rentals.html">Bin Rentals</a></li>
            <li><a href="portable-toilets.html">Portable Toilets</a></li>
            <li><a href="temporary-fencing.html">Temporary Fencing</a></li>
            <li><a href="commercial-services.html">Commercial</a></li>
            <li><a href="residential-services.html">Residential</a></li>
            <li><a href="contractor.html">Contractors</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Bin Sizes</h4>
          <ul>
            <li><a href="rentals.html#yard12">12-Yard &mdash; $210+</a></li>
            <li><a href="rentals.html#yard20">20-Yard &mdash; $245+</a></li>
            <li><a href="rentals.html#yard30">30-Yard &mdash; $275+</a></li>
            <li><a href="rentals.html#yard40">40-Yard &mdash; $325+</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Contact</h4>
          <ul>
            <li><a href="tel:4034611677">(403) 461-1677</a></li>
            <li><a href="mailto:info@avalanchewm.com">info@avalanchewm.com</a></li>
            <li><a href="booking.html">Book Online</a></li>
            <li><a href="contact.html">Contact Us</a></li>
          </ul>
          <p style="font-size:.82rem;margin-top:14px;opacity:.7;">#1, 2419 &ndash; 52 Ave SE<br/>Calgary, Alberta T2C 4X7</p>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2024 Avalanche Waste Management Calgary. All rights reserved.</p>
        <p>Serving Calgary &amp; Surrounding Area, Alberta</p>
      </div>
    </div>
  </footer>

  <!-- ── Mobile nav auto-close ──────────────────────────
       The CSS-only checkbox hack keeps the menu open after
       a link tap. This script unchecks the toggle whenever
       any nav link (including dropdown items) is clicked.
  ─────────────────────────────────────────────────────── -->
  <script>
    (function () {{
      var toggle = document.getElementById('nav-toggle');
      if (!toggle) return;
      document.querySelectorAll('.nav-link, .dropdown-item').forEach(function (el) {{
        el.addEventListener('click', function () {{
          toggle.checked = false;
        }});
      }});
    }})();
  </script>

</body>
</html>'''
    path = os.path.join(BASE, filename)
    with open(path, 'w') as f:
        f.write(html)
    print(f"  wrote {filename} ({len(html):,} chars)")

# ── ABOUT ──────────────────────────────────────────────────────────────────────
page("about.html",
  "About | Avalanche Waste Management Calgary",
  "Learn about Avalanche Waste Management — Calgary's award-winning bin rental company built on honesty, integrity, fair pricing, and recycling.",
  "about",
  "assets/kent.jpg",
  '''  <!-- ── Hero ───────────────────────────────────────────── -->
  <section class="page-hero">
    <div class="container page-hero-content">
      <p class="breadcrumb"><a href="index.html">Home</a> &rsaquo; About</p>
      <h1>About Avalanche Waste Management</h1>
      <p>Built on honesty, integrity, and a deep commitment to Calgary&rsquo;s community and environment.</p>
    </div>
  </section>

  <!-- ── Story ──────────────────────────────────────────── -->
  <section class="section">
    <div class="container">
      <div class="split split-2-3">
        <div class="hide-mobile">
          <img src="assets/kent.jpg" alt="Kenton Van Doesburg — President, Avalanche Waste Management" style="max-height:420px;" loading="lazy" />
        </div>
        <div>
          <span class="label">Our Story</span>
          <h2 class="h2">Calgary&rsquo;s Innovative Waste Management Leader</h2>
          <p style="color:var(--gray);margin-top:12px;">At Avalanche Waste Management, we take pride in our green initiatives and doing our part in taking care of the environment. Our bins are manufactured right here in Southern Alberta &mdash; supporting local businesses while delivering best-in-class equipment to our customers.</p>
          <p style="color:var(--gray);margin-top:12px;">A large majority of the junk and waste we haul is recycled and repurposed &mdash; including construction waste, wood, metal, cardboard, and drywall &mdash; diverting materials from landfills as an important part of our business model.</p>
          <p style="color:var(--gray);margin-top:12px;">We specialize in making waste management one less problem on your plate. Whether you&rsquo;re a busy site supervisor or a homeowner tackling a renovation, we show up on time, charge a fair price, and take care of the rest.</p>
          <p style="margin-top:18px;font-weight:700;">Kenton Van Doesburg &mdash; President &amp; Owner</p>
          <div class="btn-group mt-24">
            <a class="btn btn-primary" href="contact.html">Contact Us</a>
            <a class="btn btn-outline" href="booking.html">Book a Bin</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ── Values ─────────────────────────────────────────── -->
  <section class="section bg-light">
    <div class="container">
      <div class="text-center mb-48">
        <span class="label">Our Commitments</span>
        <h2 class="h2">What We Stand For</h2>
        <p class="lead mx-auto">Four unbreakable principles guide every job we take on.</p>
      </div>
      <div class="split">
        <div>
          <div class="feature-list">
            <div class="feature-item">
              <div class="feature-icon"><img src="assets/icon-honesty.png" alt="" /></div>
              <div class="feature-text">
                <h4>Honesty and Integrity</h4>
                <p>Our junk removal reputation is important to us and we always strive to improve it. We conduct business with the utmost honesty and integrity when dealing with our loyal customers.</p>
              </div>
            </div>
            <div class="feature-item">
              <div class="feature-icon"><img src="assets/icon-fair-pricing.png" alt="" /></div>
              <div class="feature-text">
                <h4>Fair Pricing and No Hidden Fees</h4>
                <p>The price of the roll-off bin, along with the dump fees and handling fees, is what you pay for. No fuel surcharge, environmental fees, or other nasty hidden surprises.</p>
              </div>
            </div>
            <div class="feature-item">
              <div class="feature-icon"><img src="assets/icon-quality.png" alt="" /></div>
              <div class="feature-text">
                <h4>Quality Service, Always</h4>
                <p>We commit to fulfilling orders within 24 hours. We handle on-site relocations, last-minute requests, and after-hours needs to keep your project on schedule.</p>
              </div>
            </div>
            <div class="feature-item">
              <div class="feature-icon" style="background:var(--green2);"><span class="emoji">&#9851;</span></div>
              <div class="feature-text">
                <h4>Environmental Responsibility</h4>
                <p>We recycle and repurpose a large majority of the waste we collect &mdash; construction material, wood, metal, cardboard, drywall &mdash; to divert as much as possible from landfills.</p>
              </div>
            </div>
          </div>
        </div>
        <div class="hide-mobile">
          <img src="assets/service-bins.jpg" alt="Avalanche WM bins" style="max-height:500px;" loading="lazy" />
        </div>
      </div>
    </div>
  </section>

  <!-- ── Awards ─────────────────────────────────────────── -->
  <section class="awards-bar">
    <div class="container">
      <h2>Recognized for Excellence</h2>
      <p>We&rsquo;re proud to be Calgary&rsquo;s award-winning waste management company.</p>
      <div class="awards-logos">
        <div><img src="assets/award-consumer-choice.png" alt="2020 Consumer Choice Award" /></div>
        <div><img src="assets/award-top-choice.png" alt="2018-2019 Top Choice Award" /></div>
        <div class="award-bbb"><img src="assets/bbb-logo.png" alt="BBB Accredited Business" /></div>
      </div>
    </div>
  </section>

  <!-- ── Testimonial ────────────────────────────────────── -->
  <section class="section">
    <div class="container" style="max-width:760px;">
      <div class="text-center mb-32">
        <span class="label">What Clients Say</span>
        <h2 class="h2">Trusted by Calgary&rsquo;s Best</h2>
      </div>
      <div class="testimonial-block">
        <div class="testimonial-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p class="testimonial-text">&ldquo;Avalanche Waste Management is an exceptional garbage removal service. They are on time and honest for a great value. The employees are top notch drivers and pickup of the bins is done in a timely fashion. I would recommend them for all garbage needs. I continue to use their service and am very pleased to continue working with them.&rdquo;</p>
        <div class="testimonial-author"><strong>Chris Levesque</strong><span>Owner, Levesque Roofing Inc.</span></div>
      </div>
    </div>
  </section>

  <!-- ── CTA ────────────────────────────────────────────── -->
  <section class="cta-banner">
    <h2>Ready to Work With Us?</h2>
    <p>Call <a href="tel:4034611677" style="color:#8be5b0;font-weight:700;">403-461-1677</a> or book online &mdash; no hidden fees, guaranteed.</p>
    <div class="btn-group" style="justify-content:center;">
      <a class="btn btn-white" href="booking.html">Book a Bin Online</a>
      <a class="btn btn-ghost" href="contact.html">Get in Touch</a>
    </div>
  </section>'''
)

# ── COMMERCIAL ────────────────────────────────────────────────────────────────
page("commercial-services.html",
  "Commercial Services | Avalanche Waste Management Calgary",
  "Avalanche WM specializes in commercial bin rentals and waste management for contractors, builders, roofers, and businesses. No hidden fees. Call 403-461-1677.",
  "commercial",
  "assets/commercial-banner.jpg",
  '''  <!-- ── Hero ───────────────────────────────────────────── -->
  <section class="page-hero">
    <div class="container">
      <div class="page-hero-content page-hero-photo">
        <div>
          <p class="breadcrumb"><a href="index.html">Home</a> &rsaquo; <a href="#">Services</a> &rsaquo; Commercial</p>
          <h1>Commercial Services</h1>
          <p>Permanent and on-demand waste management solutions for businesses, contractors, and builders across Calgary.</p>
          <div class="btn-group">
            <a class="btn btn-white" href="booking.html">Book Today</a>
            <a class="btn btn-ghost" href="tel:4034611677">Call 403-461-1677</a>
          </div>
        </div>
        <div>
          <img src="assets/commercial-banner.jpg" alt="Commercial bin rental Calgary" loading="eager" />
        </div>
      </div>
    </div>
  </section>

  <!-- ── Overview ───────────────────────────────────────── -->
  <section class="section">
    <div class="container">
      <div class="split split-3-2">
        <div>
          <span class="label">Commercial Waste Management</span>
          <h2 class="h2">Capacity to Handle the Waste</h2>
          <p style="color:var(--gray);margin-top:12px;">We specialize in bin rentals and waste management for commercial companies that require permanent or high-frequency waste bin solutions. If your business generates more waste than a standard front-loading bin can handle, we&rsquo;re the right fit.</p>
          <p style="color:var(--gray);margin-top:12px;">Your business can have a permanent bin on location, and as soon as it fills, Avalanche Waste Management services the bin and returns it empty &mdash; keeping your operations running without interruption.</p>
          <p style="color:var(--gray);margin-top:12px;">We strive to provide best-in-class customer service and use our years of experience to make waste management an easy part of operating your business.</p>

          <h3 style="margin-top:28px;margin-bottom:14px;">Industries We Serve</h3>
          <div class="tag-list">
            <span class="tag">Custom Home Builders</span>
            <span class="tag">Roofing Contractors</span>
            <span class="tag">Home Renovators</span>
            <span class="tag">Flooring Contractors</span>
            <span class="tag">Drywall Contractors</span>
            <span class="tag">Service Businesses</span>
            <span class="tag">High Dry Waste Turnover</span>
          </div>

          <div class="notice mt-24">
            <strong>No hidden fees or environmental fees, no fuel surcharges, and no cost recovery charges.</strong> When we tell you a price, that is the price you pay.
          </div>

          <div class="btn-group mt-32">
            <a class="btn btn-primary" href="booking.html">Book Today</a>
            <a class="btn btn-outline" href="contact.html">Request a Quote</a>
          </div>
        </div>
        <div class="hide-mobile">
          <img src="assets/bin-commercial.png" alt="Commercial bin" style="max-height:480px;" loading="lazy" />
        </div>
      </div>
    </div>
  </section>

  <!-- ── Bin Sizes ───────────────────────────────────────── -->
  <section class="section bg-light">
    <div class="container">
      <div class="text-center mb-48">
        <span class="label">Available Bins</span>
        <h2 class="h2">Commercial Bin Sizes</h2>
        <p class="lead mx-auto">Our 30 and 40-yard bins are ideal for high-volume commercial work. We&rsquo;ll help you determine the right size and pickup schedule for your budget.</p>
      </div>
      <div class="pricing-grid">
        <div class="pricing-card featured" id="yard40">
          <div class="badge">Commercial Exclusive</div>
          <img src="assets/bin-commercial.png" alt="40-yard bin" loading="lazy" />
          <h3>40-Yard Bin</h3>
          <div class="price">$325 <small>+ disposal</small></div>
          <ul class="spec-list">
            <li>Dimensions: 21&rsquo; &times; 7.5&rsquo; &times; 7&rsquo;</li>
            <li>High-capacity for shake tear-offs</li>
            <li>Contractors &amp; builders exclusive</li>
            <li>Includes delivery &amp; pick-up</li>
            <li>$8/day after 7-day period</li>
          </ul>
          <a class="btn btn-primary btn-block" href="booking.html">Book Now</a>
        </div>
        <div class="pricing-card" id="yard30">
          <img src="assets/bin-commercial.png" alt="30-yard bin" loading="lazy" />
          <h3>30-Yard Bin</h3>
          <div class="price">$275 <small>+ disposal</small></div>
          <ul class="spec-list">
            <li>Dimensions: 16&rsquo; &times; 8&rsquo; &times; 6&rsquo;</li>
            <li>Large roofing &amp; demo projects</li>
            <li>Contractors &amp; builders exclusive</li>
            <li>Includes delivery &amp; pick-up</li>
            <li>$8/day after 7-day period</li>
          </ul>
          <a class="btn btn-primary btn-block" href="booking.html">Book Now</a>
        </div>
        <div class="pricing-card">
          <img src="assets/bin-residential.png" alt="20-yard bin" loading="lazy" />
          <h3>20-Yard Bin</h3>
          <div class="price">$245 <small>+ disposal</small></div>
          <ul class="spec-list">
            <li>Dimensions: 16&rsquo; &times; 7&rsquo; &times; 5&rsquo;</li>
            <li>Medium-scale commercial projects</li>
            <li>Includes delivery &amp; pick-up</li>
            <li>$8/day after 7-day period</li>
          </ul>
          <a class="btn btn-primary btn-block" href="booking.html">Book Now</a>
        </div>
        <div class="pricing-card">
          <img src="assets/bin-residential.png" alt="12-yard bin" loading="lazy" />
          <h3>12-Yard Bin</h3>
          <div class="price">$210 <small>+ disposal</small></div>
          <ul class="spec-list">
            <li>Dimensions: 12&rsquo; &times; 6&rsquo; &times; 4.5&rsquo;</li>
            <li>Small commercial &amp; mixed-use</li>
            <li>Includes delivery &amp; pick-up</li>
            <li>$8/day after 7-day period</li>
          </ul>
          <a class="btn btn-primary btn-block" href="booking.html">Book Now</a>
        </div>
      </div>
    </div>
  </section>

  <!-- ── Awards ─────────────────────────────────────────── -->
  <section class="awards-bar">
    <div class="container">
      <h2>Recognized for Excellence</h2>
      <p>Calgary&rsquo;s award-winning waste management company.</p>
      <div class="awards-logos">
        <div><img src="assets/award-consumer-choice.png" alt="2020 Consumer Choice Award" /></div>
        <div><img src="assets/award-top-choice.png" alt="2018-2019 Top Choice Award" /></div>
        <div class="award-bbb"><img src="assets/bbb-logo.png" alt="BBB Accredited Business" /></div>
      </div>
    </div>
  </section>

  <!-- ── CTA ────────────────────────────────────────────── -->
  <section class="cta-banner">
    <h2>Let&rsquo;s Find Your Solution</h2>
    <p>We&rsquo;ll work with you to determine the right bin size and schedule for your budget. Call <a href="tel:4034611677" style="color:#8be5b0;font-weight:700;">403-461-1677</a> or book online.</p>
    <div class="btn-group" style="justify-content:center;">
      <a class="btn btn-white" href="booking.html">Book a Bin Online</a>
      <a class="btn btn-ghost" href="contact.html">Request a Quote</a>
    </div>
  </section>'''
)

# ── RESIDENTIAL ───────────────────────────────────────────────────────────────
page("residential-services.html",
  "Residential Services | Avalanche Waste Management Calgary",
  "Bin rentals for Calgary homeowners — renovations, repairs, and cleanouts. Transparent pricing, no hidden fees. Call 403-461-1677.",
  "residential",
  "assets/residential-banner.jpg",
  '''  <!-- ── Hero ───────────────────────────────────────────── -->
  <section class="page-hero">
    <div class="container">
      <div class="page-hero-content page-hero-photo">
        <div>
          <p class="breadcrumb"><a href="index.html">Home</a> &rsaquo; <a href="#">Services</a> &rsaquo; Residential</p>
          <h1>Residential Services</h1>
          <p>Renovating your home or working on some repairs? A bin outside your home might be just what you need to keep your workspace free from clutter.</p>
          <div class="btn-group">
            <a class="btn btn-white" href="booking.html">Book Today</a>
            <a class="btn btn-ghost" href="contact.html">Get a Quote</a>
          </div>
        </div>
        <div>
          <img src="assets/residential-banner.jpg" alt="Residential bin rental Calgary" loading="eager" />
        </div>
      </div>
    </div>
  </section>

  <!-- ── Overview ───────────────────────────────────────── -->
  <section class="section">
    <div class="container">
      <div class="split split-2-3">
        <div class="hide-mobile">
          <img src="assets/bin-residential-photo.jpg" alt="Residential bin delivery" style="max-height:460px;" loading="lazy" />
        </div>
        <div>
          <span class="label">For Homeowners</span>
          <h2 class="h2">Exceptional Service and Value</h2>
          <p style="color:var(--gray);margin-top:12px;">You can count on Avalanche Waste Management to provide exceptional service and value. We have a variety of sizes that work for your specific project and the materials you will be disposing of.</p>
          <p style="color:var(--gray);margin-top:12px;">We will work with you to make sure we find the optimal drop-off and pick-up dates for your project schedule. We consult with you on placement and size, and will help our customers through the entire process from ordering services to final pick-up.</p>
          <p style="color:var(--gray);margin-top:12px;">We provide top of the line service each step of the way.</p>

          <div class="feature-list mt-24">
            <div class="feature-item">
              <div class="feature-icon"><img src="assets/icon-honesty.png" alt="" /></div>
              <div class="feature-text">
                <h4>Consultation Included</h4>
                <p>We consult with you on bin placement and size selection to ensure you get the right solution for your project.</p>
              </div>
            </div>
            <div class="feature-item">
              <div class="feature-icon"><img src="assets/icon-fair-pricing.png" alt="" /></div>
              <div class="feature-text">
                <h4>No Hidden Fees</h4>
                <p>No hidden fees, no environmental fees, no fuel surcharges, and no cost recovery charges. The price we quote is the price you pay.</p>
              </div>
            </div>
            <div class="feature-item">
              <div class="feature-icon"><img src="assets/icon-quality.png" alt="" /></div>
              <div class="feature-text">
                <h4>Flexible Scheduling</h4>
                <p>Evening and weekend delivery available. We work around your schedule to make the process as seamless as possible.</p>
              </div>
            </div>
          </div>

          <div class="btn-group mt-32">
            <a class="btn btn-primary" href="booking.html">Book Today</a>
            <a class="btn btn-outline" href="rentals.html">View All Pricing</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ── Residential Bins ────────────────────────────────── -->
  <section class="section bg-light">
    <div class="container">
      <div class="text-center mb-48">
        <span class="label">Residential Bin Sizes</span>
        <h2 class="h2">Right-Sized for Your Project</h2>
        <p class="lead mx-auto">From small cleanouts to large renovations &mdash; we have a bin that fits your driveway and your budget.</p>
      </div>
      <div class="pricing-grid">
        <div class="pricing-card featured" id="res-y20">
          <div class="badge">Most Popular</div>
          <img src="assets/bin-residential.png" alt="20-yard bin" loading="lazy" />
          <h3>20-Yard Bin</h3>
          <div class="price">$245 <small>+ disposal</small></div>
          <ul class="spec-list">
            <li>Dimensions: 16&rsquo; &times; 7&rsquo; &times; 5&rsquo;</li>
            <li>Fits standard residential driveway</li>
            <li>Ideal for large renos &amp; cleanouts</li>
            <li>Includes delivery &amp; pick-up</li>
            <li>$8/day after 7-day period</li>
          </ul>
          <a class="btn btn-primary btn-block" href="booking.html">Book Now</a>
        </div>
        <div class="pricing-card" id="res-y12">
          <img src="assets/bin-residential.png" alt="12-yard bin" loading="lazy" />
          <h3>12-Yard Bin</h3>
          <div class="price">$210 <small>+ disposal</small></div>
          <ul class="spec-list">
            <li>Dimensions: 12&rsquo; &times; 6&rsquo; &times; 4.5&rsquo;</li>
            <li>Multi-purpose residential solution</li>
            <li>Fits a standard parking stall</li>
            <li>Includes delivery &amp; pick-up</li>
            <li>$8/day after 7-day period</li>
          </ul>
          <a class="btn btn-primary btn-block" href="booking.html">Book Now</a>
        </div>
      </div>
      <div class="notice mt-24">Also need a portable toilet or temporary fencing for your project? <a href="contact.html" style="color:var(--green);font-weight:700;">Contact us</a> for a combined quote.</div>
    </div>
  </section>

  <!-- ── Awards ─────────────────────────────────────────── -->
  <section class="awards-bar">
    <div class="container">
      <h2>Recognized for Excellence</h2>
      <p>Calgary&rsquo;s award-winning waste management company.</p>
      <div class="awards-logos">
        <div><img src="assets/award-consumer-choice.png" alt="2020 Consumer Choice Award" /></div>
        <div><img src="assets/award-top-choice.png" alt="2018-2019 Top Choice Award" /></div>
        <div class="award-bbb"><img src="assets/bbb-logo.png" alt="BBB Accredited Business" /></div>
      </div>
    </div>
  </section>

  <!-- ── CTA ────────────────────────────────────────────── -->
  <section class="cta-banner">
    <h2>Let&rsquo;s Get Started</h2>
    <p>Call <a href="tel:4034611677" style="color:#8be5b0;font-weight:700;">403-461-1677</a> or book your bin online. No hidden fees, guaranteed.</p>
    <div class="btn-group" style="justify-content:center;">
      <a class="btn btn-white" href="booking.html">Book a Bin Online</a>
      <a class="btn btn-ghost" href="contact.html">Send Us a Message</a>
    </div>
  </section>'''
)

# ── RENTALS ───────────────────────────────────────────────────────────────────
page("rentals.html",
  "Bin Rentals & Pricing | Avalanche Waste Management Calgary",
  "Affordable bin rental rates in Calgary. 12, 20, 30, and 40-yard roll-off bins. Prices include delivery and pick-up. No hidden fees. Book online or call 403-461-1677.",
  "rentals",
  "assets/service-bins.jpg",
  '''  <!-- ── Hero ───────────────────────────────────────────── -->
  <section class="page-hero">
    <div class="container page-hero-content">
      <p class="breadcrumb"><a href="index.html">Home</a> &rsaquo; Bin Rentals</p>
      <h1>AWM Rental Rates</h1>
      <p>Affordable pricing on bin rentals &amp; packages. All prices include delivery and pick-up &mdash; no hidden fees, no fuel surcharges.</p>
      <div class="btn-group">
        <a class="btn btn-white" href="booking.html">Book Today</a>
        <a class="btn btn-ghost" href="tel:4034611677">Call 403-461-1677</a>
      </div>
    </div>
  </section>

  <!-- ── Pricing intro ──────────────────────────────────── -->
  <section class="section-sm">
    <div class="container text-center">
      <span class="label">Selecting the Right Dumpster Rental Solution</span>
      <h2 class="h2">Calgary&rsquo;s Best Bin Rental Solution</h2>
      <p class="lead mx-auto">We are Calgary&rsquo;s best bin rental solution. We have a variety of different junk removal and roll-off bin sizes to choose from. A large majority of junk and waste we haul is recycled and repurposed, diverting it from landfills.</p>
      <div class="notice mt-16 mx-auto" style="max-width:700px;text-align:left;">
        <strong>Pricing note:</strong> Starting prices include delivery and pick-up. Disposal fees (TBD) are determined at the landfill based on weight and material type. Bins kept beyond 7 days incur a $8/day extension fee.
      </div>
    </div>
  </section>

  <!-- ── Commercial Bins ────────────────────────────────── -->
  <section class="section bg-light">
    <div class="container">
      <div class="text-center mb-48">
        <span class="label">Commercial Bins</span>
        <h2 class="h2">Contractors &amp; Builders</h2>
        <p class="lead mx-auto">Our larger bins are designed for high-volume commercial work &mdash; shake tear-offs, major renovations, and large construction projects.</p>
      </div>
      <div class="pricing-grid">
        <div class="pricing-card featured" id="yard40">
          <div class="badge">Contractors Exclusive</div>
          <img src="assets/bin-commercial.png" alt="40-yard commercial bin" loading="lazy" />
          <h3>40-Yard Bin</h3>
          <div class="price">$325 <small>+ disposal</small></div>
          <ul class="spec-list">
            <li>Dimensions: 21&rsquo; &times; 7.5&rsquo; &times; 7&rsquo;</li>
            <li>High-capacity for shake tear-offs</li>
            <li>Reserved for contractors &amp; builders</li>
            <li>Includes delivery &amp; pick-up</li>
            <li>$8/day after initial 7-day period</li>
            <li>Disposal fee: TBD at landfill</li>
          </ul>
          <a class="btn btn-primary btn-block" href="booking.html">Book Now</a>
        </div>
        <div class="pricing-card" id="yard30">
          <img src="assets/bin-commercial.png" alt="30-yard commercial bin" loading="lazy" />
          <h3>30-Yard Bin</h3>
          <div class="price">$275 <small>+ disposal</small></div>
          <ul class="spec-list">
            <li>Dimensions: 16&rsquo; &times; 8&rsquo; &times; 6&rsquo;</li>
            <li>Roofing, demo, large reno projects</li>
            <li>Contractors &amp; builders</li>
            <li>Includes delivery &amp; pick-up</li>
            <li>$8/day after initial 7-day period</li>
            <li>Disposal fee: TBD at landfill</li>
          </ul>
          <a class="btn btn-primary btn-block" href="booking.html">Book Now</a>
        </div>
      </div>
    </div>
  </section>

  <!-- ── Residential Bins ────────────────────────────────── -->
  <section class="section">
    <div class="container">
      <div class="text-center mb-48">
        <span class="label">Residential Bins</span>
        <h2 class="h2">Homeowners &amp; Small Projects</h2>
        <p class="lead mx-auto">Our residential bins fit standard driveways and are perfect for home renovations, yard cleanouts, and mixed-material disposal.</p>
      </div>
      <div class="pricing-grid">
        <div class="pricing-card featured" id="yard20">
          <div class="badge">Most Popular</div>
          <img src="assets/bin-residential.png" alt="20-yard residential bin" loading="lazy" />
          <h3>20-Yard Bin</h3>
          <div class="price">$245 <small>+ disposal</small></div>
          <ul class="spec-list">
            <li>Dimensions: 16&rsquo; &times; 7&rsquo; &times; 5&rsquo;</li>
            <li>Fits a standard residential driveway</li>
            <li>Ideal for construction &amp; large cleanouts</li>
            <li>Includes delivery &amp; pick-up</li>
            <li>$8/day after initial 7-day period</li>
            <li>Disposal fee: TBD at landfill</li>
          </ul>
          <a class="btn btn-primary btn-block" href="booking.html">Book Now</a>
        </div>
        <div class="pricing-card" id="yard12">
          <img src="assets/bin-residential.png" alt="12-yard residential bin" loading="lazy" />
          <h3>12-Yard Bin</h3>
          <div class="price">$210 <small>+ disposal</small></div>
          <ul class="spec-list">
            <li>Dimensions: 12&rsquo; &times; 6&rsquo; &times; 4.5&rsquo;</li>
            <li>Multi-purpose residential solution</li>
            <li>Fits a standard parking stall</li>
            <li>Includes delivery &amp; pick-up</li>
            <li>$8/day after initial 7-day period</li>
            <li>Disposal fee: TBD at landfill</li>
          </ul>
          <a class="btn btn-primary btn-block" href="booking.html">Book Now</a>
        </div>
      </div>
    </div>
  </section>

  <!-- ── Testimonial ────────────────────────────────────── -->
  <section class="section bg-light">
    <div class="container" style="max-width:760px;">
      <div class="text-center mb-32">
        <span class="label">AVALANCHE TESTIMONIALS</span>
        <h2 class="h2">What Our Clients Say</h2>
      </div>
      <div class="testimonial-block">
        <div class="testimonial-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p class="testimonial-text">&ldquo;Avalanche Waste Management is an exceptional garbage removal service. They are on time and honest for a great value. The employees are top notch drivers and pickup of the bins is done in a timely fashion. I would recommend them for all garbage needs. I continue to use their service and am very pleased to continue working with them.&rdquo;</p>
        <div class="testimonial-author"><strong>Chris Levesque</strong><span>Owner, Levesque Roofing Inc.</span></div>
      </div>
    </div>
  </section>

  <!-- ── Awards ─────────────────────────────────────────── -->
  <section class="awards-bar">
    <div class="container">
      <h2>Recognized for Excellence</h2>
      <p>Calgary&rsquo;s award-winning waste management company.</p>
      <div class="awards-logos">
        <div><img src="assets/award-consumer-choice.png" alt="2020 Consumer Choice Award" /></div>
        <div><img src="assets/award-top-choice.png" alt="2018-2019 Top Choice Award" /></div>
        <div class="award-bbb"><img src="assets/bbb-logo.png" alt="BBB Accredited Business" /></div>
      </div>
    </div>
  </section>

  <!-- ── CTA ────────────────────────────────────────────── -->
  <section class="cta-banner">
    <h2>Ready to Book?</h2>
    <p>Call <a href="tel:4034611677" style="color:#8be5b0;font-weight:700;">403-461-1677</a> or book your bin online. No hidden fees, guaranteed.</p>
    <div class="btn-group" style="justify-content:center;">
      <a class="btn btn-white" href="booking.html">Book a Bin Online</a>
      <a class="btn btn-ghost" href="contact.html">Ask a Question</a>
    </div>
  </section>'''
)

# ── PORTABLE TOILETS ──────────────────────────────────────────────────────────
page("portable-toilets.html",
  "Portable Toilets Calgary | Avalanche Waste Management Calgary",
  "Calgary portable toilet rentals for construction, events, stampede breakfasts, and more. Weekly cleaning, 24/7 service, fair pricing. Call 403-461-1677.",
  "toilets",
  "assets/service-toilets.jpg",
  '''  <!-- ── Hero ───────────────────────────────────────────── -->
  <section class="page-hero">
    <div class="container">
      <div class="page-hero-content page-hero-photo">
        <div>
          <p class="breadcrumb"><a href="index.html">Home</a> &rsaquo; Portable Toilets</p>
          <h1>Calgary Porta Potty Rentals</h1>
          <p>Portable toilet rentals made simple &mdash; for construction sites, special events, and everything in between. Clean, reliable, and fairly priced.</p>
          <div class="btn-group">
            <a class="btn btn-white" href="booking.html">Book Today</a>
            <a class="btn btn-ghost" href="contact.html">Get a Quote</a>
          </div>
        </div>
        <div>
          <img src="assets/service-toilets.jpg" alt="Portable toilet rentals Calgary" loading="eager" />
        </div>
      </div>
    </div>
  </section>

  <!-- ── Overview ───────────────────────────────────────── -->
  <section class="section">
    <div class="container">
      <div class="split split-3-2">
        <div>
          <span class="label">Portable Toilet Rentals Made Simple</span>
          <h2 class="h2">We Serve Both the Commercial and Public Sector</h2>
          <p style="color:var(--gray);margin-top:12px;">Avalanche Waste Management is a Calgary and surrounding area portable toilet rental provider. Our rentals include weekly professional cleaning and sanitization, restocking of toilet paper and hand sanitizer, and fresh septic solution.</p>
          <p style="color:var(--gray);margin-top:12px;">Whether you need one unit for a residential renovation or 50 for a major public event, we have the capacity and experience to deliver.</p>

          <h3 style="margin-top:28px;margin-bottom:12px;">Each Rental Service Includes</h3>
          <ul class="spec-list">
            <li>Empty and refill with fresh clean fluid</li>
            <li>Refill toilet paper and hand sanitizer</li>
            <li>Clean and disinfect interior surfaces</li>
            <li>Weekly professional servicing</li>
            <li>Emergency servicing available 24/7</li>
            <li>Nightly cleanouts available for events</li>
          </ul>

          <h3 style="margin-top:24px;margin-bottom:12px;">Applications We Serve</h3>
          <div class="tag-list">
            <span class="tag">Commercial Construction</span>
            <span class="tag">New Home Builds</span>
            <span class="tag">Infills &amp; Townhouses</span>
            <span class="tag">Apartment Buildings</span>
            <span class="tag">Renovations</span>
            <span class="tag">Hazardous Sites</span>
            <span class="tag">Outdoor Festivals</span>
            <span class="tag">Concerts</span>
            <span class="tag">Special Events</span>
            <span class="tag">Stampede Breakfasts</span>
            <span class="tag">Utility &amp; Road Work</span>
            <span class="tag">Garden Centers</span>
          </div>

          <div class="btn-group mt-32">
            <a class="btn btn-primary" href="booking.html">Book Today</a>
            <a class="btn btn-outline" href="contact.html">Get a Quote</a>
          </div>
        </div>
        <div class="hide-mobile">
          <img src="assets/portable-toilets.jpg" alt="Portable toilets at event" style="max-height:500px;" loading="lazy" />
        </div>
      </div>
    </div>
  </section>

  <!-- ── Key Values ─────────────────────────────────────── -->
  <section class="section bg-light">
    <div class="container">
      <div class="text-center mb-48">
        <span class="label">Our Key Values</span>
        <h2 class="h2">Why Choose Avalanche for Portable Toilets</h2>
      </div>
      <div class="cards-grid">
        <div class="card">
          <div style="padding:28px 24px 0;"><img src="assets/icon-honesty.png" alt="" style="width:48px;height:48px;object-fit:contain;" /></div>
          <div class="card-body">
            <h3>Honesty and Integrity</h3>
            <p>Our top priority is making sure our business is run with the utmost honesty and integrity when dealing with our loyal customers.</p>
          </div>
        </div>
        <div class="card">
          <div style="padding:28px 24px 0;"><img src="assets/icon-24hr.png" alt="" style="width:48px;height:48px;object-fit:contain;" /></div>
          <div class="card-body">
            <h3>24-Hour Delivery &amp; Nightly Cleanouts</h3>
            <p>Avalanche Waste Management can deliver a rental porta-potty to your site within 24 hours or less. Nightly cleanouts available for events.</p>
          </div>
        </div>
        <div class="card">
          <div style="padding:28px 24px 0;"><img src="assets/icon-calendar.png" alt="" style="width:48px;height:48px;object-fit:contain;" /></div>
          <div class="card-body">
            <h3>Monthly Servicing</h3>
            <p>Our service contracts include weekly servicing of portable toilet rentals to ensure clean, sanitary conditions throughout your rental period.</p>
          </div>
        </div>
        <div class="card">
          <div style="padding:28px 24px 0;"><img src="assets/icon-fair-pricing.png" alt="" style="width:48px;height:48px;object-fit:contain;" /></div>
          <div class="card-body">
            <h3>Fair Pricing, No Hidden Fees</h3>
            <p>Transparent pricing. No fuel surcharge, environmental fees, or other nasty hidden surprises. When we tell you a price, that is the price you pay.</p>
          </div>
        </div>
        <div class="card">
          <div style="padding:28px 24px 0;font-size:2.5rem;">&#127914;</div>
          <div class="card-body">
            <h3>No Event Too Big or Too Small</h3>
            <p>We successfully service a wide variety of event types &mdash; from small residential renovations to large-scale outdoor festivals with hundreds of attendees.</p>
          </div>
        </div>
        <div class="card">
          <div style="padding:28px 24px 0;font-size:2.5rem;">&#128222;</div>
          <div class="card-body">
            <h3>Emergency Service Available</h3>
            <p>Need an extra unit or emergency cleanout? We&rsquo;re available around the clock to make sure your event or job site is never left without a solution.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ── Awards ─────────────────────────────────────────── -->
  <section class="awards-bar">
    <div class="container">
      <h2>Recognized for Excellence</h2>
      <p>Calgary&rsquo;s award-winning waste management company.</p>
      <div class="awards-logos">
        <div><img src="assets/award-consumer-choice.png" alt="2020 Consumer Choice Award" /></div>
        <div><img src="assets/award-top-choice.png" alt="2018-2019 Top Choice Award" /></div>
        <div class="award-bbb"><img src="assets/bbb-logo.png" alt="BBB Accredited Business" /></div>
      </div>
    </div>
  </section>

  <!-- ── Testimonial ────────────────────────────────────── -->
  <section class="section bg-light">
    <div class="container" style="max-width:760px;">
      <div class="testimonial-block">
        <div class="testimonial-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p class="testimonial-text">&ldquo;Avalanche Waste Management is an exceptional garbage removal service. They are on time and honest for a great value. The employees are top notch drivers and pickup of the bins is done in a timely fashion. I would recommend them for all garbage needs. I continue to use their service and am very pleased to continue working with them.&rdquo;</p>
        <div class="testimonial-author"><strong>Chris Levesque</strong><span>Owner, Levesque Roofing Inc.</span></div>
      </div>
    </div>
  </section>

  <!-- ── CTA ────────────────────────────────────────────── -->
  <section class="cta-banner">
    <h2>Need a Portable Toilet in Calgary?</h2>
    <p>Call <a href="tel:4034611677" style="color:#8be5b0;font-weight:700;">403-461-1677</a> or contact us online &mdash; we can deliver within 24 hours.</p>
    <div class="btn-group" style="justify-content:center;">
      <a class="btn btn-white" href="booking.html">Book Online</a>
      <a class="btn btn-ghost" href="contact.html">Get a Quote</a>
    </div>
  </section>'''
)

# ── TEMPORARY FENCING ─────────────────────────────────────────────────────────
page("temporary-fencing.html",
  "Temporary Fencing Calgary | Avalanche Waste Management Calgary",
  "Temporary fence rentals in Calgary — strong, durable, easy-to-use 10'x6' steel panels. Construction, events, hazardous sites. Call 403-461-1677.",
  "fencing",
  "assets/service-fence.jpg",
  '''  <!-- ── Hero ───────────────────────────────────────────── -->
  <section class="page-hero">
    <div class="container">
      <div class="page-hero-content page-hero-photo">
        <div>
          <p class="breadcrumb"><a href="index.html">Home</a> &rsaquo; Temporary Fencing</p>
          <h1>Temporary Fencing Calgary</h1>
          <p>Strong, durable, and easy to use. Temporary fencing for construction sites, events, hazardous areas, and everything in between.</p>
          <div class="btn-group">
            <a class="btn btn-white" href="contact.html">Get a Quote</a>
            <a class="btn btn-ghost" href="tel:4034611677">Call 403-461-1677</a>
          </div>
        </div>
        <div>
          <img src="assets/service-fence.jpg" alt="Temporary fencing Calgary" loading="eager" />
        </div>
      </div>
    </div>
  </section>

  <!-- ── Overview ───────────────────────────────────────── -->
  <section class="section">
    <div class="container">
      <div class="split split-2-3">
        <div class="hide-mobile">
          <img src="assets/fencing.jpg" alt="Temporary fencing panels" style="max-height:480px;" loading="lazy" />
        </div>
        <div>
          <span class="label">Calgary Temporary Fencing</span>
          <h2 class="h2">Reliable Fence Rentals to Secure Any Perimeter</h2>
          <p style="color:var(--gray);margin-top:12px;">Serving Calgary and surrounding area, Avalanche Waste Management provides temporary fencing for many different needs. Our fence rentals allow you to secure any perimeter without having to add any permanent structures.</p>
          <p style="color:var(--gray);margin-top:12px;">Our panels measure <strong>10 feet wide by 6 feet in height</strong> and feature solid steel construction throughout, including fasteners and locking equipment. Designed to withstand uneven ground and adverse terrain, our light-weight panels include strong cross-bracing for maximum stability.</p>

          <div class="feature-list mt-28">
            <div class="feature-item">
              <div class="feature-icon"><span class="emoji">&#9940;</span></div>
              <div class="feature-text">
                <h4>Professional Panels</h4>
                <p>10&rsquo; wide &times; 6&rsquo; tall steel panels with strong cross-bracing, fasteners, and locking equipment.</p>
              </div>
            </div>
            <div class="feature-item">
              <div class="feature-icon"><span class="emoji">&#127959;</span></div>
              <div class="feature-text">
                <h4>Built for Tough Conditions</h4>
                <p>Designed to withstand uneven ground, adverse terrain, and Calgary&rsquo;s variable weather conditions.</p>
              </div>
            </div>
            <div class="feature-item">
              <div class="feature-icon"><span class="emoji">&#128197;</span></div>
              <div class="feature-text">
                <h4>Flexible Rental Periods</h4>
                <p>Short-term for events or long-term for construction projects. We accommodate your schedule and project timeline.</p>
              </div>
            </div>
            <div class="feature-item">
              <div class="feature-icon"><img src="assets/icon-fair-pricing.png" alt="" /></div>
              <div class="feature-text">
                <h4>Fair, Transparent Pricing</h4>
                <p>No hidden fees or environmental fees, no fuel surcharges. When we tell you a price, that is the price you pay.</p>
              </div>
            </div>
          </div>

          <div class="btn-group mt-32">
            <a class="btn btn-primary" href="contact.html">Get a Quote</a>
            <a class="btn btn-outline" href="tel:4034611677">Call Us Today</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ── Applications ────────────────────────────────────── -->
  <section class="section bg-light">
    <div class="container">
      <div class="text-center mb-40">
        <span class="label">Applications</span>
        <h2 class="h2">Serving All Sectors</h2>
        <p class="lead mx-auto">Our temporary fencing solutions accommodate a wide range of commercial, residential, and event needs.</p>
      </div>
      <div class="cards-grid">
        <div class="card">
          <div style="padding:28px 24px 4px;font-size:2.2rem;">&#127959;</div>
          <div class="card-body">
            <h3>Construction Sites</h3>
            <p>Secure perimeters for commercial builds, new home construction, apartment buildings, infills, and major renovations.</p>
          </div>
        </div>
        <div class="card">
          <div style="padding:28px 24px 4px;font-size:2.2rem;">&#127927;</div>
          <div class="card-body">
            <h3>Events &amp; Festivals</h3>
            <p>Crowd control and perimeter security for outdoor concerts, festivals, stampede breakfasts, and public gatherings.</p>
          </div>
        </div>
        <div class="card">
          <div style="padding:28px 24px 4px;font-size:2.2rem;">&#9888;</div>
          <div class="card-body">
            <h3>Hazardous &amp; Utility Sites</h3>
            <p>Temporary barriers for disaster quarantines, hazardous areas, road repairs, and utility work zones.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ── Awards ─────────────────────────────────────────── -->
  <section class="awards-bar">
    <div class="container">
      <h2>Recognized for Excellence</h2>
      <p>Calgary&rsquo;s award-winning waste management company.</p>
      <div class="awards-logos">
        <div><img src="assets/award-consumer-choice.png" alt="2020 Consumer Choice Award" /></div>
        <div><img src="assets/award-top-choice.png" alt="2018-2019 Top Choice Award" /></div>
        <div class="award-bbb"><img src="assets/bbb-logo.png" alt="BBB Accredited Business" /></div>
      </div>
    </div>
  </section>

  <!-- ── CTA ────────────────────────────────────────────── -->
  <section class="cta-banner">
    <h2>Need Temporary Fencing in Calgary?</h2>
    <p>Call <a href="tel:4034611677" style="color:#8be5b0;font-weight:700;">403-461-1677</a> or send us a message for a fast quote.</p>
    <div class="btn-group" style="justify-content:center;">
      <a class="btn btn-white" href="contact.html">Get a Quote</a>
      <a class="btn btn-ghost" href="tel:4034611677">Call Us Now</a>
    </div>
  </section>'''
)

# ── CONTRACTOR ────────────────────────────────────────────────────────────────
page("contractor.html",
  "Contractors | Avalanche Waste Management Calgary",
  "Great contractor rates on Calgary bin rentals. Custom bins, evening/weekend availability, no hidden fees. Avalanche WM has deep roots in the construction industry.",
  "contractor",
  "assets/bin-commercial.png",
  '''  <!-- ── Hero ───────────────────────────────────────────── -->
  <section class="page-hero">
    <div class="container">
      <div class="page-hero-content page-hero-photo">
        <div>
          <p class="breadcrumb"><a href="index.html">Home</a> &rsaquo; Contractors</p>
          <div class="hero-badge" style="display:inline-flex;gap:6px;align-items:center;background:rgba(255,255,255,.15);border:1px solid rgba(255,255,255,.3);border-radius:100px;padding:5px 14px;font-size:.77rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;margin-bottom:18px;">Great Contracting Rates</div>
          <h1>Selecting the Right Dumpster Rental Solution</h1>
          <p>Avalanche Waste Management was founded with deep roots in the construction industry. We understand what contractors need &mdash; and we deliver.</p>
          <div class="btn-group">
            <a class="btn btn-white" href="booking.html">Book Today</a>
            <a class="btn btn-ghost" href="contact.html">Request a Quote</a>
          </div>
        </div>
        <div>
          <img src="assets/bin-commercial.png" alt="Commercial contractor bin" loading="eager" />
        </div>
      </div>
    </div>
  </section>

  <!-- ── Overview ───────────────────────────────────────── -->
  <section class="section">
    <div class="container">
      <div class="split split-3-2">
        <div>
          <span class="label">Built for Contractors</span>
          <h2 class="h2">Calgary&rsquo;s Best Bin Rental Solution</h2>
          <p style="color:var(--gray);margin-top:12px;">We are Calgary&rsquo;s best bin rental solution. We have a variety of different junk removal and roll-off bin sizes to choose from. Avalanche Waste Management was founded with deep roots in the construction industry, giving us a unique understanding of what contractors and site supervisors need.</p>
          <p style="color:var(--gray);margin-top:12px;">We know that on-site dumpsters are a small part of the overall project, but play a significant role in the success of your projects. That&rsquo;s why we aim to never become one more problem on a busy site-supervisor&rsquo;s already overwhelming schedule.</p>
          <p style="color:var(--gray);margin-top:12px;">Small in feel but with plenty of resources &mdash; we offer prompt, friendly service and from being available evenings and weekends to ordering custom bins to suit your needs, we won&rsquo;t stop until you&rsquo;re happy.</p>

          <div class="feature-list mt-28">
            <div class="feature-item">
              <div class="feature-icon"><img src="assets/icon-honesty.png" alt="" /></div>
              <div class="feature-text">
                <h4>Honesty and Integrity</h4>
                <p>Our top priority when dealing with contractors and commercial clients. Your reputation is on the line on every job &mdash; ours is too.</p>
              </div>
            </div>
            <div class="feature-item">
              <div class="feature-icon"><img src="assets/icon-24hr.png" alt="" /></div>
              <div class="feature-text">
                <h4>24-Hour Delivery Available</h4>
                <p>Need a bin tomorrow? We can deliver a bin to your site within 24 hours or less &mdash; evenings and weekends included.</p>
              </div>
            </div>
            <div class="feature-item">
              <div class="feature-icon"><span class="emoji">&#128295;</span></div>
              <div class="feature-text">
                <h4>Custom Bins to Suit Your Needs</h4>
                <p>Not all jobs are the same. We work with you to find the right bin size, pickup frequency, and schedule to match your project.</p>
              </div>
            </div>
            <div class="feature-item">
              <div class="feature-icon"><img src="assets/icon-fair-pricing.png" alt="" /></div>
              <div class="feature-text">
                <h4>No Event Too Big or Too Small</h4>
                <p>We serve all different clients no matter how small or large their project. Competitive contractor pricing with no hidden fees.</p>
              </div>
            </div>
          </div>

          <div class="btn-group mt-32">
            <a class="btn btn-primary" href="booking.html">Book Today</a>
            <a class="btn btn-outline" href="contact.html">Send Us an Email</a>
          </div>
        </div>
        <div class="hide-mobile">
          <img src="assets/service-bins.jpg" alt="Contractor bins" style="max-height:480px;" loading="lazy" />
        </div>
      </div>
    </div>
  </section>

  <!-- ── Pricing ────────────────────────────────────────── -->
  <section class="section bg-light">
    <div class="container">
      <div class="text-center mb-48">
        <span class="label">Contractor Pricing</span>
        <h2 class="h2">Rates Built for the Job Site</h2>
        <p class="lead mx-auto">Competitive pricing with no hidden fees. All bins include delivery and pick-up.</p>
      </div>
      <div class="pricing-grid">
        <div class="pricing-card featured" id="con-y40">
          <div class="badge">Contractors Exclusive</div>
          <img src="assets/bin-commercial.png" alt="40-yard bin" loading="lazy" />
          <h3>40-Yard Bin</h3>
          <div class="price">$325 <small>+ disposal</small></div>
          <ul class="spec-list">
            <li>21&rsquo; &times; 7.5&rsquo; &times; 7&rsquo;</li>
            <li>High-capacity shake tear-offs</li>
            <li>Includes delivery &amp; pick-up</li>
            <li>$8/day after 7 days</li>
          </ul>
          <a class="btn btn-primary btn-block" href="booking.html">Book Now</a>
        </div>
        <div class="pricing-card" id="con-y30">
          <img src="assets/bin-commercial.png" alt="30-yard bin" loading="lazy" />
          <h3>30-Yard Bin</h3>
          <div class="price">$275 <small>+ disposal</small></div>
          <ul class="spec-list">
            <li>16&rsquo; &times; 8&rsquo; &times; 6&rsquo;</li>
            <li>Roofing, demo, large renos</li>
            <li>Includes delivery &amp; pick-up</li>
            <li>$8/day after 7 days</li>
          </ul>
          <a class="btn btn-primary btn-block" href="booking.html">Book Now</a>
        </div>
        <div class="pricing-card" id="con-y20">
          <img src="assets/bin-residential.png" alt="20-yard bin" loading="lazy" />
          <h3>20-Yard Bin</h3>
          <div class="price">$245 <small>+ disposal</small></div>
          <ul class="spec-list">
            <li>16&rsquo; &times; 7&rsquo; &times; 5&rsquo;</li>
            <li>Mid-size construction projects</li>
            <li>Includes delivery &amp; pick-up</li>
            <li>$8/day after 7 days</li>
          </ul>
          <a class="btn btn-primary btn-block" href="booking.html">Book Now</a>
        </div>
        <div class="pricing-card" id="con-y12">
          <img src="assets/bin-residential.png" alt="12-yard bin" loading="lazy" />
          <h3>12-Yard Bin</h3>
          <div class="price">$210 <small>+ disposal</small></div>
          <ul class="spec-list">
            <li>12&rsquo; &times; 6&rsquo; &times; 4.5&rsquo;</li>
            <li>Small site or interior work</li>
            <li>Includes delivery &amp; pick-up</li>
            <li>$8/day after 7 days</li>
          </ul>
          <a class="btn btn-primary btn-block" href="booking.html">Book Now</a>
        </div>
      </div>
    </div>
  </section>

  <!-- ── Contact form snippet ────────────────────────────── -->
  <section class="section">
    <div class="container" style="max-width:720px;">
      <div class="text-center mb-32">
        <span class="label">Get In Contact</span>
        <h2 class="h2">Submit Your Request</h2>
        <p class="lead mx-auto">Fill out the form below and our team will get back to you with great contractor pricing.</p>
      </div>
      <div class="contact-form-wrap">
        <form action="https://formsubmit.co/info@avalanchewm.com" method="POST">
          <input type="hidden" name="_subject" value="Contractor Quote Request — Avalanche WM" />
          <input type="hidden" name="_captcha" value="false" />
          <div class="form-row">
            <div class="form-group">
              <label for="c-name">Full Name</label>
              <input type="text" id="c-name" name="name" required placeholder="Jane Smith" />
            </div>
            <div class="form-group">
              <label for="c-phone">Phone Number</label>
              <input type="tel" id="c-phone" name="phone" placeholder="403-xxx-xxxx" />
            </div>
          </div>
          <div class="form-group">
            <label for="c-email">Email Address</label>
            <input type="email" id="c-email" name="email" required placeholder="you@company.com" />
          </div>
          <div class="form-group">
            <label for="c-inquiry">Inquiry Type</label>
            <select id="c-inquiry" name="inquiry">
              <option value="">Select inquiry…</option>
              <option>Bins &amp; Dump Trailers</option>
              <option>Temporary Fencing</option>
              <option>Portable Toilets</option>
              <option>Ongoing Commercial Contract</option>
              <option>Other</option>
            </select>
          </div>
          <div class="form-group">
            <label for="c-info">Additional Information</label>
            <textarea id="c-info" name="message" placeholder="Project details, job site address, frequency needed…"></textarea>
          </div>
          <button type="submit" class="btn btn-primary btn-block form-submit">Send Request</button>
        </form>
      </div>
    </div>
  </section>

  <!-- ── Awards ─────────────────────────────────────────── -->
  <section class="awards-bar">
    <div class="container">
      <h2>Recognized for Excellence</h2>
      <p>Calgary&rsquo;s award-winning waste management company.</p>
      <div class="awards-logos">
        <div><img src="assets/award-consumer-choice.png" alt="2020 Consumer Choice Award" /></div>
        <div><img src="assets/award-top-choice.png" alt="2018-2019 Top Choice Award" /></div>
        <div class="award-bbb"><img src="assets/bbb-logo.png" alt="BBB Accredited Business" /></div>
      </div>
    </div>
  </section>

  <!-- ── CTA ────────────────────────────────────────────── -->
  <section class="cta-banner">
    <h2>Ready for Great Contractor Rates?</h2>
    <p>Call <a href="tel:4034611677" style="color:#8be5b0;font-weight:700;">403-461-1677</a> or email <a href="mailto:info@avalanchewm.com" style="color:#8be5b0;">info@avalanchewm.com</a> today.</p>
    <div class="btn-group" style="justify-content:center;">
      <a class="btn btn-white" href="booking.html">Book a Bin Online</a>
      <a class="btn btn-ghost" href="contact.html">Send Us an Email</a>
    </div>
  </section>'''
)

# ── CONTACT ───────────────────────────────────────────────────────────────────
page("contact.html",
  "Contact | Avalanche Waste Management Calgary",
  "Contact Avalanche Waste Management Calgary. Phone: 403-461-1677. Email: info@avalanchewm.com. Address: #1, 2419-52 Ave SE, Calgary, AB T2C 4X7.",
  "contact",
  "assets/logo.png",
  '''  <!-- ── Hero ───────────────────────────────────────────── -->
  <section class="page-hero">
    <div class="container page-hero-content">
      <p class="breadcrumb"><a href="index.html">Home</a> &rsaquo; Contact</p>
      <h1>Contact Us Today</h1>
      <p>Honesty &middot; Integrity &middot; Fair Pricing &middot; Quality Service &middot; Always!</p>
    </div>
  </section>

  <!-- ── Contact Content ────────────────────────────────── -->
  <section class="section">
    <div class="container">
      <div class="split">
        <div>
          <span class="label">Get In Touch</span>
          <h2 class="h2">We&rsquo;re Here to Help</h2>
          <p class="lead" style="max-width:100%;margin-top:12px;">Have a question about bin sizes, scheduling, portable toilets, or temporary fencing? Reach out &mdash; we&rsquo;ll help you find the right solution for your project and budget.</p>

          <div style="margin-top:32px;">
            <div class="contact-detail">
              <div class="contact-icon"><img src="assets/icon-office.png" alt="" /></div>
              <div class="contact-detail-body">
                <strong>Head Office</strong>
                <span>#1, 2419 &ndash; 52 Ave SE<br/>Calgary, Alberta T2C 4X7</span>
              </div>
            </div>
            <div class="contact-detail">
              <div class="contact-icon">&#128222;</div>
              <div class="contact-detail-body">
                <strong>Phone</strong>
                <a href="tel:4034611677">(403) 461-1677</a>
              </div>
            </div>
            <div class="contact-detail">
              <div class="contact-icon">&#9993;</div>
              <div class="contact-detail-body">
                <strong>Email</strong>
                <a href="mailto:info@avalanchewm.com">info@avalanchewm.com</a>
              </div>
            </div>
            <div class="contact-detail">
              <div class="contact-icon"><img src="assets/icon-social.png" alt="" /></div>
              <div class="contact-detail-body">
                <strong>Social Media</strong>
                <div style="display:flex;gap:12px;margin-top:6px;">
                  <a href="https://www.facebook.com/Avalanche-Waste-Management-693811640731460" target="_blank" rel="noopener" style="color:var(--green);font-weight:700;">Facebook</a>
                  <a href="https://twitter.com/avalanche_waste" target="_blank" rel="noopener" style="color:var(--green);font-weight:700;">Twitter</a>
                  <a href="https://instagram.com/avalanche_waste" target="_blank" rel="noopener" style="color:var(--green);font-weight:700;">Instagram</a>
                </div>
              </div>
            </div>
          </div>

          <div class="notice mt-24">
            <strong>Evening &amp; weekend delivery available.</strong> We commit to fulfilling orders within 24 hours.
          </div>

          <div class="btn-group mt-28">
            <a class="btn btn-primary" href="booking.html">Book a Bin Online</a>
          </div>
        </div>

        <div class="contact-form-wrap">
          <h3>Send Us a Message</h3>
          <form action="https://formsubmit.co/info@avalanchewm.com" method="POST">
            <input type="hidden" name="_subject" value="Contact Form Submission — Avalanche WM" />
            <input type="hidden" name="_captcha" value="false" />
            <div class="form-row">
              <div class="form-group">
                <label for="ct-name">Full Name</label>
                <input type="text" id="ct-name" name="name" required placeholder="Jane Smith" />
              </div>
              <div class="form-group">
                <label for="ct-phone">Phone Number</label>
                <input type="tel" id="ct-phone" name="phone" placeholder="403-xxx-xxxx" />
              </div>
            </div>
            <div class="form-group">
              <label for="ct-email">Email Address</label>
              <input type="email" id="ct-email" name="email" required placeholder="you@example.com" />
            </div>
            <div class="form-group">
              <label for="ct-inquiry">Your Inquiry</label>
              <select id="ct-inquiry" name="inquiry">
                <option value="">Select a topic…</option>
                <option>Bins &amp; Dump Trailers</option>
                <option>Temporary Fencing</option>
                <option>Portable Toilets</option>
                <option>Other</option>
              </select>
            </div>
            <div class="form-group">
              <label for="ct-message">Additional Information</label>
              <textarea id="ct-message" name="message" placeholder="Tell us about your project…"></textarea>
            </div>
            <button type="submit" class="btn btn-primary btn-block form-submit">Send Message</button>
          </form>
        </div>
      </div>
    </div>
  </section>

  <!-- ── Awards ─────────────────────────────────────────── -->
  <section class="awards-bar">
    <div class="container">
      <h2>Recognized for Excellence</h2>
      <p>Calgary&rsquo;s award-winning waste management company.</p>
      <div class="awards-logos">
        <div><img src="assets/award-consumer-choice.png" alt="2020 Consumer Choice Award" /></div>
        <div><img src="assets/award-top-choice.png" alt="2018-2019 Top Choice Award" /></div>
        <div class="award-bbb"><img src="assets/bbb-logo.png" alt="BBB Accredited Business" /></div>
      </div>
    </div>
  </section>

  <!-- ── Testimonial ────────────────────────────────────── -->
  <section class="section bg-light">
    <div class="container" style="max-width:760px;">
      <div class="testimonial-block">
        <div class="testimonial-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p class="testimonial-text">&ldquo;Avalanche Waste Management is an exceptional garbage removal service. They are on time and honest for a great value. The employees are top notch drivers and pickup of the bins is done in a timely fashion. I would recommend them for all garbage needs. I continue to use their service and am very pleased to continue working with them.&rdquo;</p>
        <div class="testimonial-author"><strong>Chris Levesque</strong><span>Owner, Levesque Roofing Inc.</span></div>
      </div>
    </div>
  </section>'''
)

# ── BOOKING ───────────────────────────────────────────────────────────────────
page("booking.html",
  "Booking | Avalanche Waste Management Calgary",
  "Reserve your bin online. Fill out our quick booking form and our team will confirm your rental. No hidden fees. Serving Calgary & surrounding area.",
  "contact",
  "assets/service-bins.jpg",
  '''  <!-- ── Hero ───────────────────────────────────────────── -->
  <section class="page-hero">
    <div class="container page-hero-content">
      <p class="breadcrumb"><a href="index.html">Home</a> &rsaquo; Booking</p>
      <h1>Reserve Your Bin</h1>
      <p>Honesty &middot; Integrity &middot; Fair Pricing &middot; Quality Service &middot; Always!<br/>Fill in the form below and our team will get back to you to confirm your booking.</p>
    </div>
  </section>

  <!-- ── Booking Form ────────────────────────────────────── -->
  <section class="section">
    <div class="container">
      <div class="split split-2-3">
        <div class="hide-mobile">
          <img src="assets/bin-residential-photo.jpg" alt="Bin delivery" style="max-height:500px;" loading="lazy" />
          <div class="feature-list" style="margin-top:28px;">
            <div class="feature-item">
              <div class="feature-icon"><img src="assets/icon-fair-pricing.png" alt="" /></div>
              <div class="feature-text">
                <h4>No Hidden Fees</h4>
                <p>The price we quote is the price you pay &mdash; no surcharges, no surprises.</p>
              </div>
            </div>
            <div class="feature-item">
              <div class="feature-icon"><img src="assets/icon-24hr.png" alt="" /></div>
              <div class="feature-text">
                <h4>24-Hour Delivery</h4>
                <p>We can fulfill most orders within 24 hours, including evening and weekends.</p>
              </div>
            </div>
            <div class="feature-item">
              <div class="feature-icon"><img src="assets/icon-honesty.png" alt="" /></div>
              <div class="feature-text">
                <h4>Honest Service</h4>
                <p>We consult with you on placement and size to ensure the perfect fit.</p>
              </div>
            </div>
          </div>
        </div>

        <div class="contact-form-wrap">
          <h3>Reserve Your Bin Today</h3>
          <form action="https://formsubmit.co/info@avalanchewm.com" method="POST">
            <input type="hidden" name="_subject" value="Bin Booking Request — Avalanche WM" />
            <input type="hidden" name="_captcha" value="false" />
            <div class="form-row">
              <div class="form-group">
                <label for="b-name">Full Name *</label>
                <input type="text" id="b-name" name="name" required placeholder="Jane Smith" />
              </div>
              <div class="form-group">
                <label for="b-phone">Phone Number</label>
                <input type="tel" id="b-phone" name="phone" placeholder="403-xxx-xxxx" />
              </div>
            </div>
            <div class="form-group">
              <label for="b-email">Email Address *</label>
              <input type="email" id="b-email" name="email" required placeholder="you@example.com" />
            </div>
            <div class="form-group">
              <label for="b-bin">Type of Bin</label>
              <select id="b-bin" name="bin_type">
                <option value="">Select bin size…</option>
                <option>12-Yard Bin ($210 + disposal)</option>
                <option>20-Yard Bin ($245 + disposal)</option>
                <option>30-Yard Bin ($275 + disposal)</option>
                <option>40-Yard Bin ($325 + disposal)</option>
                <option>Portable Toilet</option>
                <option>Temporary Fencing</option>
                <option>Not sure — please advise</option>
              </select>
            </div>
            <div class="form-row">
              <div class="form-group">
                <label for="b-dropoff">Drop-Off Date</label>
                <input type="date" id="b-dropoff" name="dropoff_date" />
              </div>
              <div class="form-group">
                <label for="b-pickup">Pick-Up Date</label>
                <input type="date" id="b-pickup" name="pickup_date" />
              </div>
            </div>
            <div class="form-group">
              <label for="b-location">Drop-Off Location / Address</label>
              <input type="text" id="b-location" name="location" placeholder="123 Main St, Calgary, AB" />
            </div>
            <div class="form-group">
              <label for="b-timeslot">Ideal Timeslot</label>
              <select id="b-timeslot" name="timeslot">
                <option value="">Select preferred time…</option>
                <option>Morning (8am – 12pm)</option>
                <option>Noon (12pm – 3pm)</option>
                <option>Evening (3pm – 7pm)</option>
                <option>Flexible</option>
              </select>
            </div>
            <div class="form-group">
              <label for="b-notes">Additional Instructions</label>
              <textarea id="b-notes" name="notes" placeholder="Gate codes, placement instructions, materials to be disposed…"></textarea>
            </div>
            <button type="submit" class="btn btn-primary btn-block form-submit">Reserve My Bin</button>
          </form>
          <p style="text-align:center;margin-top:16px;font-size:.82rem;color:var(--gray-lt);">Or call us directly at <a href="tel:4034611677" style="color:var(--green);font-weight:700;">(403) 461-1677</a></p>
        </div>
      </div>
    </div>
  </section>

  <!-- ── Awards ─────────────────────────────────────────── -->
  <section class="awards-bar">
    <div class="container">
      <h2>Recognized for Excellence</h2>
      <p>Calgary&rsquo;s award-winning waste management company.</p>
      <div class="awards-logos">
        <div><img src="assets/award-consumer-choice.png" alt="2020 Consumer Choice Award" /></div>
        <div><img src="assets/award-top-choice.png" alt="2018-2019 Top Choice Award" /></div>
        <div class="award-bbb"><img src="assets/bbb-logo.png" alt="BBB Accredited Business" /></div>
      </div>
    </div>
  </section>'''
)

print("All pages generated successfully.")
