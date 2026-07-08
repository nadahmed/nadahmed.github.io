.. _chobirbaksho:

ChobirBaksho.com — Performance Engineering
==========================================

**Stack:** Laravel, AWS CloudFront, Redis

ChobirBaksho.com is a performance-focused modernization project for a legacy
Laravel e-commerce site. The work centered on making the storefront faster,
more reliable, and better prepared for real traffic loads.

What Was Improved
-----------------

The main performance bottlenecks were in asset delivery and database access.
The project addressed both by introducing more efficient caching and reducing
unnecessary server-side work.

Key improvements included:

- CDN-backed asset delivery with AWS CloudFront
- Redis-based query caching for higher throughput
- reduction in page load times for product and storefront pages
- improved user experience and conversion potential

Why It Mattered
---------------

For an e-commerce site, even small latency issues can have a measurable effect
on user retention and conversion. This project focused on the practical side of
performance engineering: identify the hot paths, reduce the cost of repeated
work, and raise the overall quality bar of the shopping experience.

Outcome
-------

The optimization work delivered a large improvement in site responsiveness and
helped transform the platform into a much more production-ready experience.

.. button-link:: https://chobirbaksho.com
   :color: primary
   :shadow:

   Visit Site
