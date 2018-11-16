# rfpkg-minimal

A fork of [fedpkg-minimal](https://fedorahosted.org/fedpkg-minimal/)
for RPM Fusion's buildsystem. rfpkg-minimal provides a script that
only downloads a package's sources.

Note: rfpkg-minimal determines if a package is in free or in nonfree
by reading ```./.git/config```. If this fails (because the git metadata
is missing), rfpkg-minimal will default to the free namespace.

## License

Like fedpkg-minimal, rfpkg-minimal is under the GPL, version 2.
See [LICENSE](LICENSE) for the full text, and [AUTHORS.md](AUTHORS.md)
for authorship information.
