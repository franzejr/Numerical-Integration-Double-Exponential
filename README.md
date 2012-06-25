#Double Exponential Integration


Like Gaussian quadrature, tanh-sinh quadrature is well suited for arbitrary-precision integration, where an accuracy of hundreds or even thousands of digits is desired. The convergence is exponential (in the discretization sense) for sufficiently well-behaved integrands: doubling the number of evaluation points roughly doubles the number of correct digits.
Tanh-sinh quadrature is less efficient than Gaussian quadrature for smooth integrands, but unlike Gaussian quadrature tends to work equally well with integrands having singularities or infinite derivatives at one or both endpoints of the integration interval. A further advantage is that the abscissas and weights are relatively easy to compute. 

The cost of calculating abscissa-weight pairs for n-digit accuracy is roughly n2 log2 n compared to n3 log n for Gaussian quadrature.Upon comparing the scheme to Gaussian quadrature and error function quadrature, Bailey et al. (2005) found that the tanh-sinh scheme "appears to be the best for integrands of the type most often encountered in experimental math research".

