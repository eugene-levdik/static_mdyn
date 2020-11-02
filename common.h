#include <vector>
#include <boost/array.hpp>

using namespace std;

const vector<double> m = {5.97E24, 1.99E30};
const int n = m.size();
const int dim = 2;

typedef boost::array<double, 8> state_type;

//const double k_diss = 1.0e16;
const double k_diss = 0.0;
const double G = 6.67430E-11;  // m^3 * s^-2 * kg^-1
