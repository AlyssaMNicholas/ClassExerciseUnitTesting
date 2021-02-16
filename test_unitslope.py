def test_unitslope():
	from unitslopetest import unitslope
	result = unitslope(1,1,2,3,3)
	expected = 5
	assert result == expected