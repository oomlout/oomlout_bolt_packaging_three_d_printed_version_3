$fn = 50;


difference() {
	union() {
		translate(v = [149.5000000000, 1.5000000000, -7.5000000000]) {
			hull() {
				translate(v = [-17.5000000000, 1.0000000000, 0]) {
					cylinder(h = 12, r = 5);
				}
				translate(v = [17.5000000000, 1.0000000000, 0]) {
					cylinder(h = 12, r = 5);
				}
				translate(v = [-17.5000000000, -1.0000000000, 0]) {
					cylinder(h = 12, r = 5);
				}
				translate(v = [17.5000000000, -1.0000000000, 0]) {
					cylinder(h = 12, r = 5);
				}
			}
		}
		translate(v = [127.0000000000, 0.5000000000, -7.5000000000]) {
			cube(size = [45, 10, 12]);
		}
		translate(v = [42.5000000000, 0, 0.0000000000]) {
			rotate(a = [0, 90, 0]) {
				cylinder(h = 5, r = 4.0000000000);
			}
		}
		translate(v = [42.5000000000, -4.0000000000, 0]) {
			cube(size = [5, 8, 7.5000000000]);
		}
		translate(v = [42.5000000000, -4.0000000000, 4.5000000000]) {
			cube(size = [5, 10.2500000000, 6]);
		}
		translate(v = [0, 0, -2.5000000000]) {
			cylinder(h = 5, r = 5.5000000000);
		}
	}
	union() {
		translate(v = [14.0000000000, 0, 0]) {
			rotate(a = [0, 90, 0]) {
				difference() {
					union() {
						linear_extrude(height = 25) {
							polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
						linear_extrude(height = 2.5000000000) {
							polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
						}
						translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
						translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
					}
					union();
				}
			}
		}
		rotate(a = [0, 0, 0.0000000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 11.2500000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 22.5000000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 33.7500000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 45.0000000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 56.2500000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 67.5000000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 78.7500000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 90.0000000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 101.2500000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 112.5000000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 123.7500000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 135.0000000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 146.2500000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 157.5000000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 168.7500000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 180.0000000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 191.2500000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 202.5000000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 213.7500000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 225.0000000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 236.2500000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 247.5000000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 258.7500000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 270.0000000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 281.2500000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 292.5000000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 303.7500000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 315.0000000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 326.2500000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 337.5000000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 348.7500000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 360.0000000000]) {
			translate(v = [7.0000000000, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = [0, 0, 45]) {
						difference() {
							union() {
								translate(v = [-1.5000000000, -1.5000000000, -2.5000000000]) {
									cube(size = [3, 3, 5]);
								}
							}
							union();
						}
					}
				}
			}
		}
		translate(v = [132.0000000000, -10.0000000000, -7.5000000000]) {
			cube(size = [6, 17, 15]);
		}
		translate(v = [143.0000000000, -10.0000000000, -7.5000000000]) {
			cube(size = [6, 17, 15]);
		}
		translate(v = [127.0000000000, 0, 0]) {
			rotate(a = [0, 90, 0]) {
				cylinder(h = 45, r = 1.8000000000);
			}
		}
		translate(v = [159.0000000000, 0, 0]) {
			cylinder(h = 5, r = 1.8000000000);
		}
		translate(v = [164.0000000000, 0, 0]) {
			cylinder(h = 5, r = 1.8000000000);
		}
		translate(v = [169.0000000000, 0, 0]) {
			cylinder(h = 5, r = 1.8000000000);
		}
		translate(v = [40.0000000000, 0, 0]) {
			rotate(a = [0, 90, 0]) {
				cylinder(h = 10, r = 1.8000000000);
			}
		}
	}
}