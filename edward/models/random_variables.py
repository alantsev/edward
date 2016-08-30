from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

from edward.models.pointmass import PointMass as distributions_PointMass
from edward.models.random_variable import RandomVariable
from edward.util import get_session

distributions = tf.contrib.distributions


class Bernoulli(RandomVariable):
  def __init__(self, *args, **kwargs):
    super(Bernoulli, self).__init__(distributions.Bernoulli, *args, **kwargs)

  def __str__(self):
    p = self.distribution.p.eval()
    return "p: \n" + p.__str__()


class Beta(RandomVariable):
  def __init__(self, *args, **kwargs):
    super(Beta, self).__init__(distributions.Beta, *args, **kwargs)

  def __str__(self):
    sess = get_session()
    a, b = sess.run([self.distribution.a, self.distribution.b])
    return "a: \n" + a.__str__() + "\n" + \
           "b: \n" + b.__str__()


class Categorical(RandomVariable):
  def __init__(self, *args, **kwargs):
    super(Categorical, self).__init__(
        distributions.Categorical, *args, **kwargs)

  def __str__(self):
    logits = self.distribution.logits.eval()
    return "logits: \n" + logits.__str__()


class Chi2(RandomVariable):
  def __init__(self, *args, **kwargs):
    super(Chi2, self).__init__(distributions.Chi2, *args, **kwargs)

  def __str__(self):
    df = self.distribution.df.eval()
    return "df: \n" + df.__str__()


class Dirichlet(RandomVariable):
  def __init__(self, *args, **kwargs):
    super(Dirichlet, self).__init__(distributions.Dirichlet, *args, **kwargs)

  def __str__(self):
    alpha = self.distribution.alpha.eval()
    return "alpha: \n" + alpha.__str__()


class DirichletMultinomial(RandomVariable):
  def __init__(self, *args, **kwargs):
    super(DirichletMultinomial, self).__init__(
        distributions.DirichletMultinomial, *args, **kwargs)

  def __str__(self):
    sess = get_session()
    n, alpha = sess.run([self.distribution.n, self.distribution.alpha])
    return "n: \n" + n.__str__() + "\n" + \
           "alpha: \n" + alpha.__str__()


class Exponential(RandomVariable):
  def __init__(self, *args, **kwargs):
    super(Exponential, self).__init__(
        distributions.Exponential, *args, **kwargs)

  def __str__(self):
    lam = self.distribution.lam.eval()
    return "lam: \n" + lam.__str__()


class Gamma(RandomVariable):
  def __init__(self, *args, **kwargs):
    super(Gamma, self).__init__(distributions.Gamma, *args, **kwargs)

  def __str__(self):
    sess = get_session()
    alpha, beta = sess.run([self.distribution.alpha, self.distribution.beta])
    return "alpha: \n" + alpha.__str__() + "\n" + \
           "beta: \n" + beta.__str__()


class InverseGamma(RandomVariable):
  def __init__(self, *args, **kwargs):
    super(InverseGamma, self).__init__(
        distributions.InverseGamma, *args, **kwargs)

  def __str__(self):
    sess = get_session()
    alpha, beta = sess.run([self.distribution.alpha, self.distribution.beta])
    return "alpha: \n" + alpha.__str__() + "\n" + \
           "beta: \n" + beta.__str__()


class Laplace(RandomVariable):
  def __init__(self, *args, **kwargs):
    super(Laplace, self).__init__(distributions.Laplace, *args, **kwargs)

  def __str__(self):
    sess = get_session()
    loc, scale = sess.run([self.distribution.loc, self.distribution.scale])
    return "loc: \n" + loc.__str__() + "\n" + \
           "scale: \n" + scale.__str__()


class MultivariateNormalCholesky(RandomVariable):
  def __init__(self, *args, **kwargs):
    super(MultivariateNormalCholesky, self).__init__(
        distributions.MultivariateNormalCholesky, *args, **kwargs)

  def __str__(self):
    sess = get_session()
    mu, chol = sess.run([self.distribution.mu, self.distribution.chol])
    return "mu: \n" + mu.__str__() + "\n" + \
           "chol: \n" + chol.__str__()


class MultivariateNormalDiag(RandomVariable):
  def __init__(self, *args, **kwargs):
    super(MultivariateNormalDiag, self).__init__(
        distributions.MultivariateNormalDiag, *args, **kwargs)

  def __str__(self):
    sess = get_session()
    mu, diag_stdev = sess.run([self.distribution.mu,
                               self.distribution.diag_stdev])
    return "mu: \n" + mu.__str__() + "\n" + \
           "diag_stdev: \n" + diag_stdev.__str__()


class MultivariateNormalFull(RandomVariable):
  def __init__(self, *args, **kwargs):
    super(MultivariateNormalFull, self).__init__(
        distributions.MultivariateNormalFull, *args, **kwargs)

  def __str__(self):
    sess = get_session()
    mu, sigma = sess.run([self.distribution.mu, self.distribution.sigma])
    return "mu: \n" + mu.__str__() + "\n" + \
           "sigma: \n" + sigma.__str__()


class Normal(RandomVariable):
  def __init__(self, *args, **kwargs):
    super(Normal, self).__init__(distributions.Normal, *args, **kwargs)

  def __str__(self):
    sess = get_session()
    mu, sigma = sess.run([self.distribution.mu, self.distribution.sigma])
    return "mu: \n" + mu.__str__() + "\n" + \
           "sigma: \n" + sigma.__str__()

  @property
  def mu(self):
    return self.distribution.mu

  @property
  def sigma(self):
    return self.distribution.sigma


class StudentT(RandomVariable):
  def __init__(self, *args, **kwargs):
    super(StudentT, self).__init__(distributions.StudentT, *args, **kwargs)

  def __str__(self):
    sess = get_session()
    df, mu, sigma = sess.run([self.distribution.df,
                              self.distribution.mu,
                              self.distribution.sigma])
    return "df: \n" + df.__str__() + "\n" + \
           "mu: \n" + mu.__str__() + "\n" + \
           "sigma: \n" + sigma.__str__()


class TransformedDistribution(RandomVariable):
  def __init__(self, *args, **kwargs):
    super(TransformedDistribution, self).__init__(
        distributions.TransformedDistribution, *args, **kwargs)

  def __str__(self):
    return self.distribution.base_distribution.__str__()


class Uniform(RandomVariable):
  def __init__(self, *args, **kwargs):
    super(Uniform, self).__init__(distributions.Uniform, *args, **kwargs)

  def __str__(self):
    sess = get_session()
    a, b = sess.run([self.distribution.a, self.distribution.b])
    return "a: \n" + a.__str__() + "\n" + \
           "b: \n" + b.__str__()


class PointMass(RandomVariable):
  def __init__(self, *args, **kwargs):
    super(PointMass, self).__init__(distributions_PointMass, *args, **kwargs)

  def __str__(self):
    params = self.distribution.params.eval()
    return "params: \n" + params.__str__()
