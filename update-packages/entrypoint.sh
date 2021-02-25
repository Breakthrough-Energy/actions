#!/bin/sh -l

cd $1
cp Pipfile.lock Pipfile.lock.old
pipenv lock --pre
summary=$(python /pkgdiff.py Pipfile.lock.old Pipfile.lock)
rm Pipfile.lock.old
echo "::set-output name=summary::$summary"
