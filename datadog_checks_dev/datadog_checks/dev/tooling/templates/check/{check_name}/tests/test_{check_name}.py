{license_header}from datadog_checks.{check_name} import {check_class}


def test_check(aggregator, instance):
    # TODO: Add tests
    # check = {check_class}('{check_name}', {{}}, {{}})
    # check.check(instance)
    print({check_class})  # import file for minimal check

    aggregator.assert_all_metrics_covered()
