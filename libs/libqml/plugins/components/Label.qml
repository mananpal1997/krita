/* This file is part of the KDE project
 * Copyright (C) 2012 Arjen Hiemstra <ahiemstra@heimr.nl>
 *
 *  SPDX-License-Identifier: GPL-2.0-or-later
 */

import QtQuick 2.3

Text {
    verticalAlignment: Text.AlignVCenter;
    color: Settings.theme.color("components/label");
    font: Settings.theme.font("application");
    elide: Text.ElideRight;
}
