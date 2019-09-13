# pyplotCDT
# README rendered with readme2tex python script
# python -m readme2tex --output README.md README.tex.md
Defect formation energy diagrams with Python

$E^{f}(D^q) = E_{\rm tot}(D^q) -  E_{\rm tot}^{\text{pristine}}- \sum_i n_i \mu_{i} + qE_{F} + \Delta^q$

where $E_{\rm tot}(D^q)$ is the total energy of a slab supercell containing the oxygen vacancy, $E_{\rm tot}^{\text{pristine}}$ is the total energy of the pristine slab, and $\mu_{i}$ is the chemical potential of species i ($n_i$ < 0 for removal of species and $n_i >0 $ is addition of species). The Fermi level $E_F$ is referenced to the valence-band maximum (VBM) of the bulk. The final term, $\Delta^q$ is a charge-state dependent correction due to the finite size of the supercell.

For details of the theory, see [10.1103/RevModPhys.86.253](https://link.aps.org/doi/10.1103/RevModPhys.86.253)
See example_fig.png for demo.
