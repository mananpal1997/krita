"""
Copyright (c) 2017 Eliakin Costa <eliakim170@gmail.com>

SPDX-License-Identifier: GPL-2.0-or-later

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
"""
from PyQt5.QtGui import QTextCursor


class DocWrapper(object):

    def __init__(self, textdocument):
        self.textdocument = textdocument

    def write(self, text, view=None):
        cursor = QTextCursor(self.textdocument)
        cursor.clearSelection()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
